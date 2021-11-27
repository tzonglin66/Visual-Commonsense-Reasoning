from typing import Dict
import torch
from allennlp.models import Model
from allennlp.data.vocabulary import Vocabulary
from allennlp.data.token_indexers import TokenIndexer, SingleIdTokenIndexer
from allennlp.data.fields.text_field import TextFieldTensors, TextField
from allennlp.data.fields import LabelField
from allennlp.data.instance import Instance
from allennlp.data.tokenizers import Tokenizer, WhitespaceTokenizer
from allennlp.data.data_loaders import SimpleDataLoader

class ToyModel(Model):
    def __init__(self, vocab: Vocabulary):
        super().__init__(vocab)

    def forward(self,
                t_tokens: TextFieldTensors,
                t_label: torch.Tensor = None) -> Dict[str, torch.Tensor]:
        print(""
              "t_tokens", t_tokens)
        print(""
              "t_label", t_label)

        return {}


tokenizer : Tokenizer = WhitespaceTokenizer()

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
data_loader = SimpleDataLoader(instances, 2, vocab=vocab)

for batch in data_loader:
    model(**batch)



