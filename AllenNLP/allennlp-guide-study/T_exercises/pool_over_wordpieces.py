from allennlp.data.tokenizers import Token
from allennlp.data.token_indexers import PretrainedTransformerMismatchedIndexer
from allennlp.data.fields import TextField
from allennlp.data.vocabulary import Vocabulary
from allennlp.modules.text_field_embedders import BasicTextFieldEmbedder
from allennlp.modules.token_embedders import PretrainedTransformerMismatchedEmbedder

text_tokens = ["This", "is", "some", "frandibulous", "text", "."]
tokens = [Token(x) for x in text_tokens]
print(tokens)

transformer_model = "google/reformer-crime-and-punishment"
token_indexer = PretrainedTransformerMismatchedIndexer(model_name=transformer_model)
token_indexers = {"transformer": token_indexer}

text_field = TextField(tokens, token_indexers)
print("text field looks like:", text_field)

text_field.index(Vocabulary())
token_tensor = text_field.as_tensor(text_field.get_padding_lengths())

print("Indexed tensors:", token_tensor)

token_embedder = PretrainedTransformerMismatchedEmbedder(model_name=transformer_model)
token_embedders = {"transformer": token_embedder}

text_field_embedder = BasicTextFieldEmbedder(token_embedders=token_embedders)

tensor_dict = text_field.batch_tensors([token_tensor])  # 相当于给tensor多加了一个维度

embedded_tokens = text_field_embedder(tensor_dict)
print("Embedded tokens size:", embedded_tokens.size())
print("Embedded tokens:", embedded_tokens)
