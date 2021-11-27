# 作 者：田宗林
# 时 间：2021/11/3
"""
torchvision.transforms.functional.resize(
    img: torch.Tensor,
    size: List[int],
    interpolation: torchvision.transforms.functional.InterpolationMode = <InterpolationMode.BILINEAR: 'bilinear'>) → torch.Tensor[SOURCE]
Resize the input image to the given size. I
f the image is torch Tensor, it is expected to have […, H, W] shape, where … means an arbitrary number of leading dimensions

Parameters:
    img (PIL Image or Tensor) – Image to be resized.
    size (sequence or int) – Desired output size.
        If size is a sequence like (h, w), the output size will be matched to this.
        If size is an int, the smaller edge of the image will be matched to this number maintaining the aspect ratio.
            i.e, if height > width, then image will be rescaled to (size×heightwidth,size).
        In torchscript mode size as single int is not supported, use a sequence of length 1: [size, ].
    interpolation (InterpolationMode) – Desired interpolation enum defined by torchvision.transforms.InterpolationMode.
        Default is InterpolationMode.BILINEAR. If input is Tensor, only InterpolationMode.NEAREST, InterpolationMode.BILINEAR and InterpolationMode.BICUBIC are supported. For backward compatibility integer values (e.g. PIL.Image.NEAREST) are still acceptable.
Returns:
    Resized image.
    Return type: PIL Image or Tensor
"""