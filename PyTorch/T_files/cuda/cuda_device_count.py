# 作 者：田宗林
# 时 间：2021/10/28
import torch

# torch.cuda.device_count()
"""
Returns the number of GPUs available.
"""

print('GPU可用数:', torch.cuda.device_count())
