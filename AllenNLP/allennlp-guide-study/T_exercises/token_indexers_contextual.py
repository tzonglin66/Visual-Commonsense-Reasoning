from allennlp.data.tokenizers import Tokenizer, WhitespaceTokenizer, PretrainedTransformerTokenizer
from allennlp.data.token_indexers import TokenIndexer, ELMoTokenCharactersIndexer, PretrainedTransformerIndexer
from allennlp.data.vocabulary import Vocabulary
from allennlp.data.fields import TextField


tokenizer: Tokenizer = WhitespaceTokenizer()

token_indexer: TokenIndexer = ELMoTokenCharactersIndexer()
token_indexers = {"elmo_tokens": token_indexer}


vocab = Vocabulary()

text = "This is some text ."
tokens = tokenizer.tokenize(text)
print("ELMo tokens:", tokens)

text_field = TextField(tokens, token_indexers)
text_field.index(vocab)
print(text_field)


padding_lengths = text_field.get_padding_lengths()

tensor_dict = text_field.as_tensor(padding_lengths)
print("ELMo tensors:", tensor_dict)


transformer_model = "bert-base-cased"

tokenizer = PretrainedTransformerTokenizer(model_name=transformer_model)

token_indexer = PretrainedTransformerIndexer(model_name=transformer_model)
token_indexers = {"bert_tokens": token_indexer}

text = "Some text with an extraordinarily long identifier."
tokens = tokenizer.tokenize(text)
print("BERT tokens:", tokens)

text_field = TextField(tokens, token_indexers)
text_field.index(vocab)
print(text_field)

tensor_dict = text_field.as_tensor(text_field.get_padding_lengths())
print("BERT tensors:", tensor_dict)


tokenizer = PretrainedTransformerTokenizer(
    model_name=transformer_model,
    add_special_tokens=False,
)

context_text = "This context is frandibulous."
question_text = "What is the context like?"
context_tokens = tokenizer.tokenize(context_text)
question_tokens = tokenizer.tokenize(question_text)
print("Context tokens:", context_tokens)
print("Question tokens:", question_tokens)

combined_tokens = tokenizer.add_special_tokens(context_tokens, question_tokens)
print("Combined tokens:", combined_tokens)

text_field = TextField(combined_tokens, token_indexers)
text_field.index(vocab)
print(text_field)

tensor_dict = text_field.as_tensor(text_field.get_padding_lengths())
print("Combined BERT tensors:", tensor_dict)
