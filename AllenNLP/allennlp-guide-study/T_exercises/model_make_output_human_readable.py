from typing import Dict
import torch
import numpy
from allennlp.models import Model
from allennlp.data.vocabulary import Vocabulary
from allennlp.data.token_indexers import TokenIndexer, SingleIdTokenIndexer
from allennlp.data.fields.text_field import TextFieldTensors, TextField
from allennlp.data.fields import LabelField
from allennlp.data.instance import Instance
from allennlp.data.tokenizers import Tokenizer, WhitespaceTokenizer


class ToyModel(Model):
    def __init__(self, vocab: Vocabulary):
        super().__init__(vocab)

    def forward(self,
                t_tokens: TextFieldTensors,
                t_label: torch.Tensor = None) -> Dict[str, torch.Tensor]:
        batch_size = t_tokens["id"]["tokens"].size()[0]  # size()方法返回tensor的维数元组
        logits = torch.normal(mean=0.0, std=1.0, size=(batch_size, 2))  # 产生batch_size行，每行两个元素服从正态分布随机的随机数
        print(logits)

        probs = torch.softmax(logits, dim=1)
        # 将logit指数正规化

        return {"logits": logits, "probs": probs}

    def make_output_human_readable(
        self, output_dict: Dict[str, torch.Tensor]
    ) -> Dict[str, torch.Tensor]:
        logits = output_dict["logits"].cpu().data.numpy()
        # cpu: 复制到cpu
        predicted_id: numpy.ndarray = numpy.argmax(logits, axis=-1)
        output_dict["label"] = [  # type: ignore
            self.vocab.get_token_from_index(x, namespace="labels") for x in predicted_id
            ]

        return output_dict


tokenizer: Tokenizer = WhitespaceTokenizer()

text_pos = "The best movie ever !"
text_neg = "Such an awful movie ."

tokens_pos = tokenizer.tokenize(text_pos)
tokens_neg = tokenizer.tokenize(text_neg)

token_indexers: Dict[str, TokenIndexer] = {"id": SingleIdTokenIndexer()}

text_field_pos = TextField(tokens_pos, token_indexers)
text_field_neg = TextField(tokens_neg, token_indexers)

label_field_pos = LabelField("pos")
label_field_neg = LabelField("neg")

fields_pos = {"t_tokens": text_field_pos, "t_label": label_field_pos}
fields_neg = {"t_tokens": text_field_neg, "t_label": label_field_neg}

instance_pos = Instance(fields_pos)
print(instance_pos)
instance_neg = Instance(fields_neg)
print(instance_neg)
instances = [instance_pos, instance_neg]


vocab = Vocabulary.from_instances(instances)
print(vocab.get_index_to_token_vocabulary(namespace="tokens"))
print(vocab.get_index_to_token_vocabulary(namespace="labels"))


model = ToyModel(vocab)

print(model.forward_on_instance(instance_pos))
print(model.forward_on_instances(instances))
