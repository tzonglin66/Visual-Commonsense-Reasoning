# 作 者：田宗林
# 时 间：2021/10/29
# torch
import torch

"""
torch.randint(low=0, high, size, 
    *, generator=None, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False) → Tensor
Returns a tensor filled with random integers generated uniformly between low (inclusive) and high (exclusive).
The shape of the tensor is defined by the variable argument size. 

Parameters
    low (int, optional) – Lowest integer to be drawn from the distribution. Default: 0.
    high (int) – One above the highest integer to be drawn from the distribution.
    size (tuple) – a tuple defining the shape of the output tensor.
"""


a = torch.randint(3, 5, (3,))
print(a)
b = torch.randint(10, (2, 2))
print(b)
c = torch.randint(3, 10, (2, 2))

print(c)


"""
torch.squeeze(input, dim=None, *, out=None) → Tensor
Returns a tensor with all the dimensions of input of size 1 removed.

Parameters
    input (Tensor) – the input tensor.
    dim (int, optional) – if given, the input will be squeezed only in this dimension
"""

x = torch.zeros(2, 1, 2, 1, 2)
print(x.size())
y = torch.squeeze(x)
print(y.size())
