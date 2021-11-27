# 作 者：田宗林
# 时 间：2021/7/10
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

# 准备测试数据集

test_data = torchvision.datasets.CIFAR10('cif_data', train=False, transform=torchvision.transforms.ToTensor())
# getitem(): <- 返回img, target

test_loader = DataLoader(dataset=test_data, batch_size=64, shuffle=True, num_workers=0, drop_last=True)
# 返回imgs, targets

# batch_size：每次提取图片的数量
# shuffle：每次提取取图片的顺序是否一致
# drop_last：最后不足一个batch_size的图片是否提取

# 测试数据集中的第一张图片及target
img, target = test_data[0]
print(img.shape)
print(target)
# print('------------------------')

writer = SummaryWriter('../cif_data/data_loader_logs')
for epoch in range(2):
    step = 0
    for data in test_loader:
        imgs, targets = data
        # print(imgs.shape)
        # print(targets)
        writer.add_images('Epoch: {}'.format(epoch), imgs, step)
        step = step + 1

writer.close()
