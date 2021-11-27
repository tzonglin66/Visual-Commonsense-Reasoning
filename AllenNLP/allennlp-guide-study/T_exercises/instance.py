from allennlp.data.tokenizers import Token
from allennlp.data.fields import Field, TextField, LabelField, SequenceLabelField
from allennlp.data.token_indexers import TokenIndexer, SingleIdTokenIndexer
from allennlp.data.instance import Instance
from typing import Dict

tokens = [Token("The"), Token("best"), Token("movie"), Token("ever"), Token("!")]
token_indexers: Dict[str, TokenIndexer] = {"tokens": SingleIdTokenIndexer()}
text_field = TextField(tokens, token_indexers=token_indexers)

label_field = LabelField("pos")

sequence_label_field = SequenceLabelField(
    ["DET", "ADJ", "NOUN", "ADV", "PUNKT"], text_field, label_namespace='labels'
)

fields: Dict[str, Field] = {
    "tokens": text_field,
    "label": label_field,
}
instance = Instance(fields)
instance.add_field("label_seq", sequence_label_field)
print(instance)
