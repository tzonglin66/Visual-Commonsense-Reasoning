# 作 者：田宗林
# 时 间：2021/10/3
import torch
from allennlp.modules.attention import (
    Attention,
    DotProductAttention,
    BilinearAttention,
    LinearAttention
)
from allennlp.modules.matrix_attention import (
    MatrixAttention,
    DotProductMatrixAttention,
    BilinearMatrixAttention,
    LinearMatrixAttention
)
from allennlp.nn import Activation

embedding_dim1 = 8
embedding_dim2 = 16
sequence_length = 10

attention: Attention

vector = torch.rand((1, embedding_dim1))
matrix = torch.rand((1, sequence_length, embedding_dim1))
attention = DotProductAttention()
output = attention(vector, matrix)

print("Output from DotProductAttention:", output)

vector = torch.rand((1, embedding_dim1))
matrix = torch.rand((1, sequence_length, embedding_dim2))
attention = BilinearAttention(vector_dim=embedding_dim1,
                              matrix_dim=embedding_dim2)
output = attention(vector, matrix)
print("Output from BilinearAttention:", output)


tanh = Activation.by_name("tanh")()
attention = LinearAttention(tensor_1_dim=embedding_dim1,
                            tensor_2_dim=embedding_dim2,
                            combination="x,y",
                            activation=tanh)
output = attention(vector, matrix)
print("Out from LinearAttention:", output)


sequence_length1 = 10
sequence_length2 = 15
matrix_attention: MatrixAttention

matrix1 = torch.rand((1, sequence_length1, embedding_dim1))
matrix2 = torch.rand((1, sequence_length2, embedding_dim1))

matrix_attention = DotProductMatrixAttention()
output = matrix_attention(matrix1, matrix2)
print("Output shape of DotProductMatrixAttention:", output.shape)

matrix1 = torch.rand((1, sequence_length1, embedding_dim1))
matrix2 = torch.rand((1, sequence_length2, embedding_dim2))

matrix_attention = BilinearMatrixAttention(
    matrix_1_dim=embedding_dim1, matrix_2_dim=embedding_dim2
)
output = matrix_attention(matrix1, matrix2)
print("Output shape of BilinearMatrixAttention:", output.shape)


matrix_attention = LinearMatrixAttention(
    tensor_1_dim=embedding_dim1,
    tensor_2_dim=embedding_dim2,
    combination="x,y",
    activation=tanh)
output = matrix_attention(matrix1, matrix2)
print("Output shape of BilinearMatrixAttention:", output.shape)
