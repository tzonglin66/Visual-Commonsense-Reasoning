"""
（1）多看官方文档 > 网上解释
（2）关注输入和输出类型【print、type、debug】
（3）关注参数
"""

from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

writer = SummaryWriter("../logs")
img = Image.open("../images/4d56b6f2d7c321bc228fd.jpg")
print(img)

# ToTensor
trans_totensor = transforms.ToTensor()
img_tensor = trans_totensor(img)
writer.add_image("ToTensor", img_tensor)

# Normalize
print(img_tensor[0][0][0])
# trans_norm = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
# trans_norm = transforms.Normalize([1, 2, 3], [3, 2, 1])
trans_norm = transforms.Normalize([2, 3, 1], [1, 2, 3])
img_norm = trans_norm(img_tensor)
print(img_norm[0][0][0])
# writer.add_image("Normalize", img_norm, 0)
# writer.add_image("Normalize", img_norm, 1)
writer.add_image("Normalize", img_norm, 2)

# Resize - 1
print(img.size)
trans_resize = transforms.Resize([512, 512])
# img PIL -> resize -> img_resize PIL
img_resize = trans_resize(img)
# img_resize PIL -> totensor -> img_resize tensor
img_resize = trans_totensor(img_resize)
print(type(img_resize))
writer.add_image("Resize", img_resize, 0)

# Compose - resize - 2
trans_resize_2 = transforms.Resize(512)
# PIL -> PIL -> Tensor
trans_compose = transforms.Compose([trans_resize_2, trans_totensor])
img_resize_2 = trans_compose(img)
writer.add_image("Resize", img_resize_2, 1)

""""
RandomCrop - 1
trans_random_crop = transforms.RandomCrop(512)
trans_compose_2 = transforms.Compose([trans_random_crop, trans_totensor])
for i in range(10):
    img_random_crop = trans_compose_2(img)
    writer.add_image("RandomCrop", img_random_crop, i)
"""

# RandomCrop - 2
trans_random_crop = transforms.RandomCrop(500, 100)
trans_compose_2 = transforms.Compose([trans_random_crop, trans_totensor])
for i in range(10):
    img_random_crop = trans_compose_2(img)
    writer.add_image("RandomCropHW", img_random_crop, i)

writer.close()
