# 作 者：田宗林
# 时 间：2021/7/19
# import torch
import torchvision
from torch import nn
from torch.utils.data import DataLoader

# input = torch.tensor([[1, -0.5],
#                      [-1, 3]])
#
# input = torch.reshape(input, (-1, 1, 2, 2))
# print(input.shape)
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10('cif_data', train=False, download=True,
                                       transform=torchvision.transforms.ToTensor())

dataloader = DataLoader(dataset, batch_size=64)


class T_module(nn.Module):
    def __init__(self):
        super(T_module, self).__init__()
        self.relu1 = nn.ReLU()
        self.sigmoid1 = nn.Sigmoid()

    def forward(self, input):
        output = self.sigmoid1(input)
        return output


t_module = T_module()
# output = t_module(input)
# print(output)
writer = SummaryWriter("../logs/relu_sigmoid")
step = 0
for data in dataloader:
    imgs, targets = data
    writer.add_images("input", imgs, step)
    output = t_module(imgs)
    writer.add_images("output", output, step)
    step = step + 1

writer.close()
