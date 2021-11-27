# 作 者：田宗林
# 时 间：2021/7/23
import torch

outputs = torch.tensor([[0.1, 0.2],
                        [0.3, 0.4]])
print(outputs.argmax(1))
preds = outputs.argmax(1)
targets = torch.tensor([0, 1])
print((preds == targets).sum())
