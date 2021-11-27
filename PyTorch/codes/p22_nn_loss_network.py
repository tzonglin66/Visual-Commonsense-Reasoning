# 作 者：田宗林
# 时 间：2021/7/21
import torchvision
from torch import nn
from torch.nn import Module, Conv2d, MaxPool2d, Linear, Sequential
from torch.nn.modules.flatten import Flatten
from torch.utils.data import DataLoader

dataset = torchvision.datasets.CIFAR10('cif_data', train=False, transform=torchvision.transforms.ToTensor(),
                                       download=True)

dataloader = DataLoader(dataset, batch_size=64)


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


loss = nn.CrossEntropyLoss()
t_module = T_Module()
for data in dataloader:
    imgs, targets = data
    outputs = t_module(imgs)
    print(outputs.shape)
    print(targets.shape)
    result_loss = loss(outputs, targets)
    print(result_loss)
