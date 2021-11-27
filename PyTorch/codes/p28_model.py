# 作 者：田宗林
# 时 间：2021/7/23

# 搭建神经网络
import torch
from torch import nn


class Tmodel(nn.Module):
    def __init__(self):
        super(Tmodel, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(64 * 4 * 4, 64),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        x = self.model(x)
        return x


if __name__ == '__main__':
    tmodel = Tmodel()
    input = torch.ones((64, 3, 32, 32))
    output = tmodel(input)
    print(output.shape)
