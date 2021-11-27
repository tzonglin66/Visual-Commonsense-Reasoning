# 作 者：田宗林
# 时 间：2021/7/24
import torch
import torchvision
from torch.utils.tensorboard import SummaryWriter

# from p28_model import *
# 准备数据集
from torch import nn
from torch.utils.data import DataLoader
import time

# 定义训练的设备
device = torch.device("cuda:0")
# 更常用写法：device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)
# device = torch.device("cuda") <----> device = torch.device("cuda:0")
# device = torch.device("cuda:n-1")

train_data = torchvision.datasets.CIFAR10(root="../cif_data", train=True, transform=torchvision.transforms.ToTensor(),
                                          download=True)
test_data = torchvision.datasets.CIFAR10(root="../cif_data", train=False, transform=torchvision.transforms.ToTensor(),
                                         download=True)

# length
train_data_size = len(train_data)
test_data_size = len(test_data)
# 如果train_data_size = 10, print输出训练数据集的长度为：10
print("训练数据集的长度为：{}".format(train_data_size))
print("测试数据集的长度为：{}".format(test_data_size))

# 利用DataLoader来加载数据
train_dataloader = DataLoader(train_data, batch_size=64)
test_dataloader = DataLoader(test_data, batch_size=64)

# 创建网络模型


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


tmodel = Tmodel()
tmodel.to(device)  # 可以不用另外赋值 <---tmodel.to(device)

# 损失函数
loss_fn = nn.CrossEntropyLoss()
loss_fn.to(device)  # 可以不用另外赋值 <---tmodel.to(device)

# 优化器
# learning rate = 0.02
learning_rate = 1e-2
optimizer = torch.optim.SGD(tmodel.parameters(), lr=learning_rate)

# 设置训练网络的一些参数
# 记录训练的次数
total_train_step = 0
# 记录测试的次数
total_test_step = 0
# 训练的轮数
epoch = 10

# 添加tensorboard
writer = SummaryWriter("../logs/train")
start_time = time.time()

for i in range(epoch):
    print("---------第 {} 轮训练开始---------".format(i+1))

    # 训练步骤开始
    tmodel.train()
    for data in train_dataloader:
        imgs, targets = data
        imgs = imgs.to(device)  # 必须另外赋值 <---tmodel.to(device)
        targets = targets.to(device)  # 必须另外赋值 <---tmodel.to(device)
        output = tmodel(imgs)
        loss = loss_fn(output, targets)

        # 优化器优化模型
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_train_step += 1
        if total_train_step % 100 == 0:
            end_time = time.time()
            print(end_time-start_time)
            print("训练次数：{}, Loss：{}".format(total_train_step, loss.item()))
            writer.add_scalar("train_loss", loss.item(), total_train_step)

    # 测试步骤开始
    tmodel.eval()
    total_test_loss = 0
    total_accuracy = 0
    with torch.no_grad():
        for data in test_dataloader:
            imgs = imgs.to(device)
            targets = targets.to(device)
            targets = targets.cuda()
            outputs = tmodel(imgs)
            loss = loss_fn(outputs, targets)
            total_test_loss += loss.item()
            accuracy = (outputs.argmax(1) == targets).sum()
            total_accuracy += accuracy.item()

    total_test_step += 1
    print("整体测试集上的loss：{}".format(total_test_loss))
    print("整体测试集上的正确率：{}".format(total_accuracy/test_data_size))
    writer.add_scalar("test_loss", total_test_loss, total_test_step)
    writer.add_scalar("test_accuracy", total_accuracy/test_data_size, total_test_step)

    # 保存模型
    torch.save(tmodel, "../model_data/tmodel_{}.pth".format(i+1))
    # torch.save(tmodel.state_dict(), "../model_data/tmodel_{}.pth".format(i+1))
    print("模型已保存")

writer.close()
