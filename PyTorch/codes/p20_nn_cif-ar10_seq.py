# 作 者：田宗林
# 时 间：2021/7/21
import torch
from torch.nn import Module, Conv2d, MaxPool2d, Linear, Sequential
from torch.nn.modules.flatten import Flatten
from torch.utils.tensorboard import SummaryWriter


class T_Module(Module):
    def __init__(self):
        super(T_Module, self).__init__()
        self.model1 = Sequential(
            Conv2d(3, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 64, 5, padding=2),
            MaxPool2d(2),
            Flatten(),
            Linear(1024, 64),  # 如果不知道In_Feature的size，可先简单验证flatten的输出
            Linear(64, 10),
        )

    def forward(self, x):
        x = self.model1(x)
        return x


t_module = T_Module()
print(t_module)

# 网络模型简单验证
input = torch.ones((64, 3, 32, 32))
output = t_module(input)
print(output.shape)

writer = SummaryWriter("../logs/seq")
writer.add_graph(t_module, input)
writer.close()
