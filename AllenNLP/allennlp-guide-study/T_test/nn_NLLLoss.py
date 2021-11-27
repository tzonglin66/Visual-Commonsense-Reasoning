# 作 者：田宗林
# 时 间：2021/8/20
# 2D loss example (used, for example, with image inputs)
import torch
N, C = 5, 4
loss = torch.nn.NLLLoss()
# input is of size N x C x height x width
data = torch.randn(N, 16, 10, 10)
conv = torch.nn.Conv2d(16, C, (3, 3))
m = torch.nn.LogSoftmax(dim=1)
# each element in target has to have 0 <= value < C
target = torch.empty(N, 8, 8, dtype=torch.long).random_(0, C)

output = loss(m(conv(data)), target)
output.backward()