# 作 者：田宗林
# 时 间：2021/7/22
import torch
import torchvision

# 模型加载方式1 <-- 保存方式1 --> 对于自己定义的model要导入“父类”定义
model1 = torch.load('model_data/vgg16_method1.pth')
print(model1)
print('------------------------------------')

# 模型加载方式2 <-- 保存方式2
model2 = torch.load('model_data/vgg16_method2.pth')
print(model2)
print('------------------------------------')
vgg16 = torchvision.models.vgg16(pretrained=False)
print(vgg16)
print('------------------------------------')
vgg16.load_state_dict(model2)
print(vgg16)
