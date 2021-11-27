# 作 者：田宗林
# 时 间：2021/10/6
# 作 者：田宗林
# 时 间：2021/10/5
from typing import Dict, Iterable, Tuple, List
import torch
from allennlp.data.dataset_readers import DatasetReader
from allennlp.data.data_loaders import DataLoader, SimpleDataLoader
from allennlp.data.tokenizers import Tokenizer, WhitespaceTokenizer
from allennlp.data.token_indexers import TokenIndexer, SingleIdTokenIndexer
from allennlp.data.instance import Instance
from allennlp.data.fields import TextField, LabelField
from allennlp.data.fields.text_field import TextFieldTensors
from allennlp.models import Model
from allennlp.data.vocabulary import Vocabulary
from allennlp.modules.text_field_embedders import TextFieldEmbedder, BasicTextFieldEmbedder
from allennlp.modules.seq2vec_encoders import Seq2VecEncoder, BagOfEmbeddingsEncoder
from allennlp.modules.token_embedders import Embedding
from allennlp.nn import util
from allennlp.training import Trainer, GradientDescentTrainer
from allennlp.training.optimizers import AdamOptimizer
from allennlp.training.metrics import CategoricalAccuracy
from allennlp.predictors import Predictor
from allennlp.common.util import JsonDict


class ClassificationTsvReader(DatasetReader):
    def __init__(
            self,
            tokenizer: Tokenizer = None,
            token_indexers: Dict[str, TokenIndexer] = None,
            max_tokens: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.tokenizer = tokenizer or WhitespaceTokenizer()
        self.token_indexers = token_indexers or {"token_id": SingleIdTokenIndexer()}
        self.max_tokens = max_tokens

    def text_to_instance(self, text: str, label: str = None) -> Instance:
        tokens = self.tokenizer.tokenize(text)
        if self.max_tokens:
            tokens = tokens[: self.max_tokens]  # 预测时保持max_tokens一致，故"上移"
        text_field = TextField(tokens, self.token_indexers)
        fields = {"text": text_field}
        if label:
            fields["label"] = LabelField(label)

        return Instance(fields)

    def _read(self, file_path: str) -> Iterable[Instance]:
        with open(file_path, "r") as lines:
            for line in lines:
                text, label = line.strip().split("\t")
                yield self.text_to_instance(text, label)


class SimpleClassifier(Model):
    def __init__(
            self,
            vocab: Vocabulary,
            embedder: TextFieldEmbedder,
            encoder: Seq2VecEncoder
    ):
        super().__init__(vocab)
        self.embedder = embedder
        self.encoder = encoder
        num_labels = vocab.get_vocab_size(namespace="labels")
        self.classifier = torch.nn.Linear(encoder.get_output_dim(), num_labels)

        # create a metric
        self.accuracy = CategoricalAccuracy()

    def forward(self,
                text: TextFieldTensors,
                label: torch.Tensor = None) -> Dict[str, torch.Tensor]:
        # Shape: (batch_size, num_tokens, embedding_dim)
        embedded_text = self.embedder(text)
        # Shape: (batch_size, num_tokens)
        mask = util.get_text_field_mask(text)
        # Shape: (batch_size, encoding_dim)
        encoded_text = self.encoder(embedded_text, mask)
        # Shape: (batch_size, num_labels)
        logits = self.classifier(encoded_text)
        # Shape: (batch_size, num_labels)
        probs = torch.nn.functional.softmax(logits, dim=-1)
        # Shape: (1,)
        output = {"probs": probs}
        if label is not None:
            loss = torch.nn.functional.cross_entropy(logits, label)
            output["loss"] = loss
            # update the metric
            self.accuracy(logits, label)

        return output

    def get_metrics(self, reset: bool = False) -> Dict[str, float]:
        """
        overwrite/implement the get_metrics method
        """
        return {"accuracy": self.accuracy.get_metric(reset)}


def build_dataset_reader() -> DatasetReader:
    return ClassificationTsvReader()


def read_data(reader: DatasetReader) -> Tuple[List[Instance], List[Instance]]:
    print("Reading data")
    training_data = list(reader.read("../data/movie_review/train.tsv"))
    validation_data = list(reader.read("../data/movie_review/dev.tsv"))

    return training_data, validation_data


def build_vocab(instances: Iterable[Instance]) -> Vocabulary:
    print("Building the vocabulary")
    return Vocabulary.from_instances(instances)


def build_model(vocab: Vocabulary) -> Model:
    print("Building the model")
    vocab_size = vocab.get_vocab_size(namespace="tokens")
    token_embedders = {"token_id": Embedding(embedding_dim=10,
                                             num_embeddings=vocab_size)}
    embedder = BasicTextFieldEmbedder(token_embedders=token_embedders)
    encoder = BagOfEmbeddingsEncoder(embedding_dim=10)

    return SimpleClassifier(vocab, embedder, encoder)


def build_data_loaders(training_data: List[Instance],
                       validation_data: List[Instance]
                       ) -> Tuple[DataLoader, DataLoader]:
    training_loader = SimpleDataLoader(training_data, 8, shuffle=True)
    validation_loader = SimpleDataLoader(validation_data, 8, shuffle=False)

    return training_loader, validation_loader


def build_trainer(
        model: Model,  # Model 是nn.Module的子类
        serialization_dir: str,
        training_loader: DataLoader,
        validation_loader: DataLoader) -> Trainer:
    parameters = [(n, p) for n, p in model.named_parameters() if p.requires_grad]  # 获取模型参数
    optimizer = AdamOptimizer(parameters)  # 参数传递给优化器
    trainer = GradientDescentTrainer(
        model=model,
        serialization_dir=serialization_dir,
        data_loader=training_loader,
        validation_loader=validation_loader,
        num_epochs=5,
        optimizer=optimizer,
        cuda_device=-1,
    )
    return trainer


# 好好体会run_training_loop的逻辑流程
# ----> 进一步体会参数的顺序依赖和Lazy类的妙用
def run_training_loop():
    dataset_reader = build_dataset_reader()

    training_data, validation_data = read_data(dataset_reader)
    vocab = build_vocab(training_data + validation_data)
    model = build_model(vocab)

    training_loader, validation_loader = build_data_loaders(training_data, validation_data)
    training_loader.index_with(vocab)
    validation_loader.index_with(vocab)
    # **********************************
    serialization_dir = "../model"
    trainer = build_trainer(model, serialization_dir, training_loader, validation_loader)
    print("Start training")
    trainer.train()  # 训练给定的模型
    print("Finished training")
    # **********************************

    # 可利用临时生成的文件夹技术tempfile.TemporaryDirectory()
    # 训练结束后创建的文件夹随即删除

    # **********************************
    # with tempfile.TemporaryDirectory() as serialization_dir:
    #     trainer = build_trainer(model, serialization_dir, train_loader, dev_loader)
    #     print("Starting training")
    #     trainer.train()
    #     print("Finished training")
    # **********************************

    return model, dataset_reader


class SentenceClassifierPredictor(Predictor):
    def predict(self, text: str) -> JsonDict:
        inputs = {"text": text}
        return self.predict_json(inputs)

    def _json_to_instance(self, json_dict: JsonDict) -> Instance:
        text = json_dict["text"]
        return self._dataset_reader.text_to_instance(text)


# run the training loop to get a trained model
model, dataset_reader = run_training_loop()
vocab = model.vocab  # Vocabulary

# create a predictor with trained model and dataset_reader
predictor = SentenceClassifierPredictor(model, dataset_reader)

text1 = "A good movie!"
output1 = predictor.predict(text1)
readable_output1 = [(vocab.get_token_from_index(label_id, "labels"), probs)
                    for label_id, probs in enumerate(output1["probs"])]  # enumerate 默认从0开始"编号"
print(readable_output1)

text2 = "This was a monstrous waste of time."
output2 = predictor.predict(text2)
readable_output2 = [(vocab.get_token_from_index(label_id, "labels"), probs)
                    for label_id, probs in enumerate(output2["probs"])]
print(readable_output2)
