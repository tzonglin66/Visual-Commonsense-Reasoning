from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

# 1. 通过transforms.ToTensor理解transforms如何使用
# 2. 为什么需要Tensor数据类型
img_path = "../dataset/hymenoptera_data/train/bees/39747887_42df2855ee.jpg"
img = Image.open(img_path)

writer = SummaryWriter("../logs")

tensor_trans = transforms.ToTensor()  # 创建了一个类
tensor_img = tensor_trans(img)

writer.add_image("Tensor_img",tensor_img)
writer.close()



