# 作 者：田宗林
# 时 间：2021/7/24
import torch
import torchvision
from PIL import Image

Image_path = "../images/airplane.png"
image = Image.open(Image_path)
image = image.convert('RGB')
print(image)

transform = torchvision.transforms.Compose([torchvision.transforms.Resize((32, 32)),
                                            torchvision.transforms.ToTensor()])

image = transform(image)
print(image.shape)

model = torch.load("../model_data/tmodel_30_gpu.pth", map_loaction=torch.device('cpu'))
print(model)

image = torch.reshape(image, (1, 3, 32, 32))
model.eval()  # 最好写上
with torch.no_grad():
    output = model(image)
print(output)

print(output.argmax(1))
