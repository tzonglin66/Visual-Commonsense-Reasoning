from allennlp.data.tokenizers import Token
from allennlp.data.token_indexers import TokenIndexer, SingleIdTokenIndexer
from allennlp.data.fields import TextField, LabelField
from allennlp.data.instance import Instance
from allennlp.data.vocabulary import Vocabulary
from typing import Dict


tokens_pos = [Token("The"), Token("best"), Token("movie"), Token("ever"), Token("!")]
tokens_neg = [Token("Such"), Token("an"), Token("awful"), Token("movie"), Token(".")]
token_indexers: Dict[str, TokenIndexer] = {
    "t1": SingleIdTokenIndexer(namespace='tokens')
}
text_field_pos = TextField(tokens_pos, token_indexers)
text_field_neg = TextField(tokens_neg, token_indexers)

label_pos = "pos"
label_neg = "neg"
label_field_pos = LabelField(label_pos)
label_field_neg = LabelField(label_neg, label_namespace="labels")

fields_pos = {"T_tokens": text_field_pos, "T_label": label_field_pos}
fields_neg = {"T_tokens": text_field_neg, "T_label": label_field_neg}

instance_pos = Instance(fields_pos)
instance_neg = Instance(fields_neg)
instances = [instance_pos, instance_neg]
print("Created instances:", instances)

vocab = Vocabulary.from_instances(instances)

print("Created a Vocabulary:", vocab)

print('index for token "movie":', vocab.get_token_index("movie"))
print('index for token "!":', vocab.get_token_index("!"))
print('index for token "unknown":', vocab.get_token_index("unknown"))

print('index for label "pos":', vocab.get_token_index("pos", namespace="labels"))
print('index for label "neg":', vocab.get_token_index("neg", namespace="labels"))

try:
    vocab.get_token_index("unknown", namespace="labels")
except KeyError:
    print('index for label "unknown": caught KeyError')
