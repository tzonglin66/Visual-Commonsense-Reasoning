# 程序员：田宗林
# 时 间：2021/7/8
import torchvision
from torch.utils.tensorboard import SummaryWriter

dataset_transform = torchvision.transforms.Compose([torchvision.transforms.ToTensor()])
# 建议download选项始终选择TRUE，若是下载较慢，可先利用讯雷下载到目标目录
# 数据集下载地址可查看对应数据集的.py文件找到url链接
train_set = torchvision.datasets.CIFAR10(root='./cif_data', train=True,
                                         transform=dataset_transform, download=True)
test_set = torchvision.datasets.CIFAR10(root='./cif_data', train=False,
                                        transform=dataset_transform, download=True)

# print(test_set[0])
# print(test_set.classes)
#
# img, target = test_set[0]
# print(img)
# print(target)
# print(test_set.classes[target])
# img.show()

writer = SummaryWriter('../cif_data/cif_logs')
for i in range(10):
    img, target = test_set[i]
    writer.add_image('test_set', img, i)

writer.close()
