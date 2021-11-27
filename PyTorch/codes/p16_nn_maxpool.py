# 作 者：田宗林
# 时 间：2021/7/19
import torch
import torchvision
from torch import nn
from torch.nn import MaxPool2d
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10('cif_data', train=False, download=True,
                                       transform=torchvision.transforms.ToTensor())

dataloader = DataLoader(dataset, batch_size=64)

# input = torch.tensor([[1, 2, 0, 3, 1],
# #                       [0, 1, 2, 3, 1],
# #                       [1, 2, 1, 0, 0],
# #                       [5, 2, 3, 1, 1],
# #                       [2, 1, 0, 1, 1]], dtype=torch.float32)
# # input = torch.reshape(input, (-1, 1, 5, 5))
# # print(input.shape)


class T_module(nn.Module):
    def __init__(self):
        super(T_module, self).__init__()
        self.maxpool1 = MaxPool2d(kernel_size=3, ceil_mode=False)

    def forward(self, input):
        output = self.maxpool1(input)
        return output


t_module = T_module()
# output = t_module(input)
# print(output)
writer = SummaryWriter("../logs/maxpool")
step = 0
for data in dataloader:
    imgs, targets = data
    writer.add_images("input", imgs, step)
    output = t_module(imgs)
    writer.add_images("output", output, step)
    step = step + 1

writer.close()
