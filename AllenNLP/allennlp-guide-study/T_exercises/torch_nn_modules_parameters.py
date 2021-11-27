# 作 者：田宗林
# 时 间：2021/10/5
import torch.nn as nn
import torch.nn.functional as f

l = nn.Linear(2, 2)
net = nn.Sequential(l, l)
# named_modules()方法返回网络中所有模块的迭代器，生成模块名称和模块本身
# Yields: (string, Module) – Tuple of name and module
for idx, m in enumerate(net.named_modules()):
    print(idx, '->', m)


# named_parameters()方法返回模块参数的迭代器，生成参数名称和参数本身
# Yields: (string, Parameter) – Tuple containing the name and parameter
for name, param in l.named_parameters():
    if name in ['bias']:
        print(param.size())

for param in l.parameters():
    print(type(param), param.size())