# 作 者：田宗林
# 时 间：2021/7/20
import torch
from torch.nn import Module, Conv2d, MaxPool2d, Linear
from torch.nn.modules.flatten import Flatten


class T_Module(Module):
    def __init__(self):
        super(T_Module, self).__init__()
        self.conv1 = Conv2d(3, 32, 5, padding=2)
        self.maxpool1 = MaxPool2d(2)
        self.conv2 = Conv2d(32, 32, 5, padding=2)
        self.maxpool2 = MaxPool2d(2)
        self.conv3 = Conv2d(32, 64, 5, padding=2)
        self.maxpool3 = MaxPool2d(2)
        self.flatten = Flatten()
        self.linear1 = Linear(1024, 64)  # 如果不知道In_Feature的size，可先简单验证flatten的输出
        self.linear2 = Linear(64, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.maxpool1(x)
        x = self.conv2(x)
        x = self.maxpool2(x)
        x = self.conv3(x)
        x = self.maxpool3(x)
        x = self.flatten(x)
        x = self.linear1(x)
        x = self.linear2(x)
        return x


t_module = T_Module()
print(t_module)

# 网络模型简单验证
input = torch.ones((64, 3, 32, 32))
output = t_module(input)
print(output.shape)