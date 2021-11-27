from allennlp.data import Tokenizer, TokenIndexer, Vocabulary
from allennlp.data.fields import TextField
from allennlp.data.tokenizers import (
    WhitespaceTokenizer,
    SpacyTokenizer
)
from allennlp.data.token_indexers import (
    SingleIdTokenIndexer,
    TokenCharactersIndexer
)

from typing import Dict

tokenizer: Tokenizer = WhitespaceTokenizer()
token_indexers: Dict[str, TokenIndexer] = {
    "index1": SingleIdTokenIndexer(namespace="t1"),
    "index2": TokenCharactersIndexer(namespace="t2"),
}

vocab = Vocabulary()
vocab.add_tokens_to_namespace(
    ["This", "is", "some", "text", "."], namespace="t1"
)
vocab.add_tokens_to_namespace(
    ["T", "h", "i", "s", " ", "o", "m", "e", "t", "x", "."],
    namespace="t2"
)

text = "This is some text ."
tokens = tokenizer.tokenize(text)
print("Tokens:", tokens)

text_field = TextField(tokens, token_indexers)
text_field.index(vocab)
padding_lengths = text_field.get_padding_lengths()
tensor_dict = text_field.as_tensor(padding_lengths)

print("Combined tensor dictionary:", tensor_dict)

tokenizer = SpacyTokenizer(pos_tags=True)
token_indexers: Dict[str, TokenIndexer] = {
    "index1": SingleIdTokenIndexer(namespace="t1"),
    "index2": TokenCharactersIndexer(namespace="t2"),
    "index3": SingleIdTokenIndexer(namespace="t3", feature_name="tag_"),
}
vocab.add_tokens_to_namespace(
    ["DT", "VBZ", "NN", "."], namespace="t3"
)

tokens = tokenizer.tokenize(text)
print("Spacy tokens:", tokens)
print("POS tags:", [token.tag_ for token in tokens])
text_field = TextField(tokens, token_indexers)
text_field.index(vocab)

padding_lengths = text_field.get_padding_lengths()

tensor_dict = text_field.as_tensor(padding_lengths)

print("Tensor dict with POS tags:", tensor_dict)
