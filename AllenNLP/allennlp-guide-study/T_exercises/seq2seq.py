import torch
from allennlp.modules.seq2seq_encoders import (
    Seq2SeqEncoder,
    PassThroughEncoder,
    LstmSeq2SeqEncoder,
)

batch_size = 8
sequence_length = 10  # 行
input_size = 5  # 列
hidden_size = 2

x = torch.rand(batch_size, sequence_length, input_size)
mask = torch.ones(batch_size, sequence_length)
print("tensor of input[0,:,:]:", x[0, :, :])
print("shape of input:", x.shape)

encoder: Seq2SeqEncoder
encoder = PassThroughEncoder(input_dim=input_size)
y = encoder(x, mask=mask)

print("tensor of output[0, :, :] (PassThrough):", y[0, :, :])
print("shape of output (PassThrough):", y.shape)

encoder = LstmSeq2SeqEncoder(input_size=input_size,
                             hidden_size=hidden_size)
y = encoder(x, mask=mask)

print("tensor of output[0, :, :] (LSTM):", y[0, :, :])
print("shape of output (LSTM):", y.shape)
