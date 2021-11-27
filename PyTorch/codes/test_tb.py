from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np


writer = SummaryWriter("/data-output")

# image_path = "dataset/hymenoptera_data/train/ants/6743948_2b8c096dda.jpg"
# image_path = "dataset/hymenoptera_data/train/bees/29494643_e3410f0d37.jpg"
image_path = "../dataset/hymenoptera_data/train/bees/39747887_42df2855ee.jpg"
img_PIL = Image.open(image_path)
img_array = np.array(img_PIL)

# writer.add_image("test", img_array, 1, dataformats='HWC')
# writer.add_image("test", img_array, 2, dataformats='HWC')
writer.add_image("train", img_array, 2, dataformats='HWC')
# y = 2x
for i in range(10):
    writer.add_scalar("y=2x", 2*i, i)

writer.close()