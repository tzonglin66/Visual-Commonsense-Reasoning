import os.path as op


USE_IMAGENET_PRETRAINED = True  # otherwise use detectron, but that doesnt seem to work?!?

# Change these to match where your annotations and images are
# op.dirname(path) 从path中提取文件（夹）所在目录路径
# __file__表示当前脚本的路径 <---- .../r2c/config.py
# op.dirname(__file__) ----> .../r2c
# .../r2c/data/vcr1images <---- 三级目录
VCR_IMAGES_DIR = op.join(op.dirname(__file__), 'data', 'vcr1images')
# .../r2c/data <---- 二级目录
VCR_ANNOTS_DIR = op.join(op.dirname(__file__), 'data')
# .../r2c/data/bert <---- 三级目录
VCR_BERTS_DIR = op.join(op.dirname(__file__), 'data', 'bert')
# op.exists(path) 判断path是否存在
if not op.exists(VCR_IMAGES_DIR):
    raise ValueError("Update config.py with where you saved VCR images to.")
