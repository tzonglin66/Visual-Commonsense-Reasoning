from allennlp.data import Tokenizer, TokenIndexer, Vocabulary
from allennlp.data.fields import TextField
from allennlp.data.tokenizers import (
    WhitespaceTokenizer,
    CharacterTokenizer
)
from allennlp.data.token_indexers import (
    SingleIdTokenIndexer,
    TokenCharactersIndexer
)

tokenizer: Tokenizer = WhitespaceTokenizer()
token_indexer: TokenIndexer = SingleIdTokenIndexer(namespace="name1")

vocab = Vocabulary()
vocab.add_tokens_to_namespace(
    ["This", "is", "some", "text", "."], namespace="name11"
)
vocab.add_tokens_to_namespace(
    ["T", "h", "i", "s", " ", "o", "m", "e", "t", "x", "."],
    namespace="name22"
)

text = "This is some text ."
tokens = tokenizer.tokenize(text)
print("Word tokens:", tokens)

text_field = TextField(tokens, {"t1": token_indexer})
text_field.index(vocab)

padding_lengths = text_field.get_padding_lengths()

tensor_dict = text_field.as_tensor(padding_lengths)

print("With single id indexer:", tensor_dict)

token_indexer = TokenCharactersIndexer(namespace="name22")
text_field = TextField(tokens, {"t2": token_indexer})
text_field.index(vocab)

padding_lengths = text_field.get_padding_lengths()

tensor_dict = text_field.as_tensor(padding_lengths)

print("With token character indexer:", tensor_dict)

tokenizer = CharacterTokenizer()

tokens = tokenizer.tokenize(text)
print("Character tokens:", tokens)

token_indexer = SingleIdTokenIndexer(namespace="name22")

text_field = TextField(tokens, {"t3": token_indexer})
text_field.index(vocab)

padding_lengths = text_field.get_padding_lengths()

tensor_dict = text_field.as_tensor(padding_lengths)

print("With single id indexer:", tensor_dict)
