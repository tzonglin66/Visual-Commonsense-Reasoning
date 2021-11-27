# 作 者：田宗林
# 时 间：2021/11/1
"""Image"""

# torchvision.io.ImageReadMode(value)
"""
Support for various modes while reading images:
    ImageReadMode.UNCHANGED: load the image as-is
    ImageReadMode.GRAY: converting to grayscale
    ImageReadMode.GRAY_ALPHA: grayscale with transparency
    ImageReadMode.RGB: RGB
    ImageReadMode.RGB_ALPHA: RGB with transparency
"""

# torchvision.io.read_image(path: str, mode: torchvision.io.image.ImageReadMode = <ImageReadMode.UNCHANGED: 0>) → torch.Tensor
"""
Reads a JPEG or PNG image into a 3 dimensional RGB Tensor. 
Optionally converts the image to the desired format. 
The values of the output tensor are uint8 between 0 and 255.

Parameters:
    path (str) – path of the JPEG or PNG image.
    mode (ImageReadMode) – the read mode used for optionally converting the image. 
        Default: ImageReadMode.UNCHANGED.

Returns:
    output (Tensor[image_channels, image_height, image_width])
"""