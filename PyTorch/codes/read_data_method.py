"""
Dataset -> 提供一种方式去获取数据及其label
    如何获取每一个数据及其label
    告诉我们总共有多少的数据
Dataloader -> 为后面的网络提供不同的数据形式
"""

from torch.utils.data import Dataset
from PIL import Image
import os


class MyData(Dataset):

    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.imgs_path = os.listdir(self.path)

    def __getitem__(self, item):
        img_item_name = self.imgs_path[item]
        img_item_path = os.path.join(self.path, img_item_name)
        img_item = Image.open(img_item_path)
        label = self.label_dir
        return img_item, label

    def __len__(self):
        return len(self.imgs_path)


data_dir = "../dataset/hymenoptera_data/train"
ants_label = "ants"
bees_label = "bees"
ants_dataset = MyData(data_dir, ants_label)
bees_dataset = MyData(data_dir, bees_label)

train_dataset = ants_dataset + bees_dataset
