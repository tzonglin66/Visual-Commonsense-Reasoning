import torch
from allennlp.modules.token_embedders import (
    Embedding,
    TokenCharactersEncoder
)
from allennlp.modules.text_field_embedders import BasicTextFieldEmbedder
from allennlp.modules.seq2vec_encoders import CnnEncoder


token_tensor = {"indexer1": {"tokens": torch.LongTensor([[1, 3, 2, 9, 4, 3]])}}

embedder = Embedding(num_embeddings=10, embedding_dim=6)
token_embedders = {"indexer1": embedder}


text_field_embedder = BasicTextFieldEmbedder(token_embedders=token_embedders)

embedded_tokens = text_field_embedder(token_tensor)
print("Using the TextFieldEmbedder:", embedded_tokens)


embedded_tokens = embedder(**token_tensor["indexer1"])
# 相当于调用embedding的forward(tokens: torch.Tensor)方法
print("Using the Embedding directly:", embedded_tokens)


token_tensor = {
    "indexer2": {
        "token_characters": torch.LongTensor(
            [[[1, 3, 0], [4, 2, 3], [1, 9, 5], [6, 0, 0]]]
        )
    }
}

character_embedder = Embedding(num_embeddings=10, embedding_dim=3)
# 输入维数3, 神经元个数为4, 只有一层卷积层，神经元大小为3*3
# 输出维数=1*4
cnn_encoder = CnnEncoder(embedding_dim=3, num_filters=4, ngram_filter_sizes=(3,))
# (3,)表示为只含3的元组, ","不可省
token_encoder = TokenCharactersEncoder(character_embedder, cnn_encoder)
token_embedders = {"indexer2": token_encoder}

text_field_embedder = BasicTextFieldEmbedder(token_embedders=token_embedders)

embedded_tokens = text_field_embedder(token_tensor)
print("With a character CNN:", embedded_tokens)
