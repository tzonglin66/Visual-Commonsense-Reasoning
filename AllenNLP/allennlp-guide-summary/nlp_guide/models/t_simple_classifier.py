# 作 者：田宗林
# 时 间：2021/10/5
from typing import Dict
import torch
from allennlp.models import Model
from allennlp.data.vocabulary import Vocabulary
from allennlp.modules.text_field_embedders import TextFieldEmbedder
from allennlp.modules.seq2vec_encoders import Seq2VecEncoder
from allennlp.data.fields.text_field import TextFieldTensors
from allennlp.training.metrics import CategoricalAccuracy
from allennlp.nn import util


@Model.register("t_simple_classifier")
class TemmSimpleClassifier(Model):
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
