# 作 者：田宗林
# 时 间：2021/7/11
# nn.conv2d
""""
weight: 卷积核
stride: 步进
padding: 填充
个数 = (n+2r-m)s+1
"""
import torch
import torch.nn.functional as fun

input = torch.tensor([[1, 2, 0, 3, 1],
                      [0, 1, 2, 3, 1],
                      [1, 2, 1, 0, 0],
                      [5, 2, 3, 1, 1],
                      [2, 1, 0, 1, 1]])
kernel = torch.tensor([[1, 2, 1],
                       [0, 1, 0],
                       [2, 1, 0]])

input = torch.reshape(input, (1, 1, 5, 5))
kernel = torch.reshape(kernel, (1, 1, 3, 3))

print(input.shape)
print(kernel.shape)

output1 = fun.conv2d(input, kernel, stride=1)
print(output1, output1.shape)

output2 = fun.conv2d(input, kernel, stride=2)
print(output2, output2.shape)

output3 = fun.conv2d(input, kernel, stride=1, padding=1)
print(output3, output3.shape)
