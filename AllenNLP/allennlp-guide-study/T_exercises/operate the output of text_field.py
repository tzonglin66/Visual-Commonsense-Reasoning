# 作 者：田宗林
# 时 间：2021/10/4
import warnings
from allennlp.data.tokenizers import SpacyTokenizer
from allennlp.data.vocabulary import Vocabulary
from allennlp.data.token_indexers import (
    SingleIdTokenIndexer,
    TokenCharactersIndexer,
)
from allennlp.data.fields import TextField, ListField
import allennlp.nn.util as nn_util
warnings.filterwarnings("ignore")  # 不打印警告信息

tokenizer = SpacyTokenizer(pos_tags=True)

vocab = Vocabulary()
vocab.add_tokens_to_namespace(["This", "is", "some", "text", "."],
                              namespace="n_token_vocab")
vocab.add_tokens_to_namespace(["T", "h", "i", "s", " ", "o", "m", "e", "t", "x", "."],
                              namespace="n_character_vocab")
# 词性含义:
# DT: 限定词、VBZ: 第三人称动词、MN: 名词
vocab. add_tokens_to_namespace(["DT", "VBZ", "MN", "."],
                               namespace="n_pos_tag_vocab")

text1 = "This is some text."
text2 = "This is some text with more tokens."
tokens1 = tokenizer.tokenize(text1)
tokens2 = tokenizer.tokenize(text2)
print("Tokens1:", tokens1)
print("Tokens2:", tokens2)

token_indexers = {
    "t_tokens": SingleIdTokenIndexer(namespace="n_token_vocab"),
    "t_token_characters": TokenCharactersIndexer(namespace="n_character_vocab"),
    "t_pos_tags": SingleIdTokenIndexer(namespace="n_pos_tag_vocab", feature_name="tag_")  # 使用tokens具有tag_属性的值
}

text_field1 = TextField(tokens1, token_indexers)
text_field1.index(vocab)
text_field2 = TextField(tokens2, token_indexers)
text_field2.index(vocab)

padding_lengths1 = text_field1.get_padding_lengths()
padding_lengths2 = text_field2.get_padding_lengths()
print("padding of text_field1:", padding_lengths1)
print("padding of text_field2:", padding_lengths2)

tensor_dict1 = text_field1.as_tensor(padding_lengths2)
tensor_dict2 = text_field2.as_tensor(padding_lengths2)

# 此结果很出乎意料但合乎情理
print("Combined tensor dictionary1:", tensor_dict1)
print("Combined tensor dictionary2:", tensor_dict2)

text_field_tensors = text_field1.batch_tensors([tensor_dict1, tensor_dict2])
print("Batched tensor dictionary:", text_field_tensors)

mask = nn_util.get_text_field_mask(text_field_tensors)
print("Mask:", mask)  # False表示padding
print("Mask size:", mask.size())

token_ids = nn_util.get_token_ids_from_text_field_tensors(text_field_tensors)
print("Token ids:", token_ids)

list_field = ListField([text_field1, text_field2, text_field1])
print("List field:", list_field)
list_padding_lengths = list_field.get_padding_lengths()
print("List padding lengths:", list_padding_lengths)

list_tensor_dict = list_field.as_tensor(list_padding_lengths)
print("List tensor dict:", list_tensor_dict)  # 第一个维度表示list长度

list_text_field_tensors = list_field.batch_tensors([list_tensor_dict])  # 增加一个batch_size维度
print("Batched List tensors:", list_text_field_tensors)
list_mask = nn_util.get_text_field_mask(list_text_field_tensors, num_wrapping_dims=1)
print("Mask:", list_mask)
print("List mask size:", list_mask.size())
