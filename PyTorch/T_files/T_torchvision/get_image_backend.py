# 作 者：田宗林
# 时 间：2021/11/3
# torchvision.get_image_backend()
"""
Gets the name of the package used to load images
"""
import torchvision as tv
print(tv.get_image_backend())  # PIL
