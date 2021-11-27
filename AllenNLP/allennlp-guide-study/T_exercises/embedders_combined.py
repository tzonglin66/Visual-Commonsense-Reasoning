import torch
from allennlp.data import Vocabulary
from allennlp.modules.token_embedders import (
    Embedding, TokenCharactersEncoder
)
from allennlp.modules.seq2vec_encoders import CnnEncoder
from allennlp.modules.text_field_embedders import BasicTextFieldEmbedder

token_tensor = {
    "t_tokens": {"n_tokens": torch.LongTensor([[2, 4, 3, 5]])},
    "t_token_characters": {
        "n_token_characters": torch.LongTensor(
            [[[2, 5, 3], [4, 0, 0], [2, 1, 4], [5, 4, 0]]]
        )
    }
}

embedding = Embedding(num_embeddings=6, embedding_dim=3)

character_embedding = Embedding(num_embeddings=6, embedding_dim=3)
cnn_encoder = CnnEncoder(embedding_dim=3, num_filters=4, ngram_filter_sizes=(3,))
token_encoder = TokenCharactersEncoder(character_embedding, cnn_encoder)

embedder = BasicTextFieldEmbedder(
    token_embedders={"t_tokens": embedding, "t_token_characters": token_encoder}
)

embedded_tokens = embedder(token_tensor)
print(embedded_tokens)

token_tensor = {
    "t_tokens": {"n_tokens": torch.LongTensor([[2, 4, 3, 5]])},
    "t_token_characters": {
        "n_token_characters": torch.LongTensor(
            [[[2, 5, 3], [4, 0, 0], [2, 1, 4], [5, 4, 0]]]
        )
    },
    "t_pos_tag_tokens": {"n_tokens": torch.LongTensor([[2, 5, 3, 4]])}
}

vocab = Vocabulary()
vocab.add_tokens_to_namespace(["This", "is", "some", "text", "."],
                              namespace="l_token_vocab")
vocab.add_tokens_to_namespace(["T", "h", "i", "s", " ", "o", "m", "e", "t", "x", "."],
                              namespace="l_character_vocab")
vocab.add_tokens_to_namespace(["Dt", "VBZ", "MN", "."], namespace="l_pos_tag_vocab")

embedding = Embedding(embedding_dim=3, vocab_namespace="l_token_vocab", vocab=vocab)
character_embedding = Embedding(embedding_dim=4, vocab_namespace="l_character_vocab", vocab=vocab)
cnn_encoder = CnnEncoder(embedding_dim=4, num_filters=5, ngram_filter_sizes=(3,))
token_encoder = TokenCharactersEncoder(character_embedding, cnn_encoder)
pos_tag_embedding = Embedding(embedding_dim=6, vocab_namespace="l_pos_tag_vocab", vocab=vocab)

embedder = BasicTextFieldEmbedder(
    token_embedders={
        "t_tokens": embedding,
        "t_token_characters": token_encoder,
        "t_pos_tag_tokens": pos_tag_embedding
    }
)
embedded_tokens = embedder(token_tensor)
print(embedded_tokens)
