# 作 者：田宗林
# 时 间：2021/7/11
# torch.nn
"""
Container: 容器（骨架） → Module
"""
import torch
from torch import nn


class Tmodule(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        output = x + 1
        return output


tmodule = Tmodule()
x = torch.tensor(1.0)
output = tmodule(x)
print(output, type(output))
