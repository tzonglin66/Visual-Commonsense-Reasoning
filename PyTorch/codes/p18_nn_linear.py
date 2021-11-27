# 作 者：田宗林
# 时 间：2021/7/20
import torch
import torchvision
from torch import nn
from torch.nn import Linear
from torch.utils.data import DataLoader

dataset = torchvision.datasets.CIFAR10('cif_data', train=False, transform=torchvision.transforms.ToTensor(),
                                       download=True)

dataloader = DataLoader(dataset, batch_size=64, drop_last=True)


class T_module(nn.Module):
    def __init__(self):
        super(T_module, self).__init__()
        self.linear1 = Linear(196608, 10)

    def forward(self, input):
        output = self.linear1(input)
        return output


t_module = T_module()

for data in dataloader:
    imgs, targets = data
    print(imgs.shape)
    # input = torch.reshape(imgs, (1, 1, 1, -1))
    input = torch.flatten(imgs)
    print(input.shape)
    output = t_module(input)
    print(output.shape)
