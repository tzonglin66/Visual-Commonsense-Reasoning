# 作 者：田宗林
# 时 间：2021/10/29
# torch.tensor
import torch


"""
# Tensor.item() → number
Returns the value of this tensor as a standard Python number.
This only works for tensors with one element. For other cases, see tolist().
"""
x = torch.tensor([1.0])
print(x.item())

"""
# Tensor.tolist() → list or number
Returns the tensor as a (nested) list. 
For scalars, a standard Python number is returned, just like with item(). 
"""
a = torch.randn(2, 2)
print(a)
print(a.tolist())
print(a[0, 0], a[0, 0].tolist())