# 作 者：田宗林
# 时 间：2021/8/12
from allennlp.common import FromParams, Params
import json


class Gaussian(FromParams):
    def __init__(self, mean: float, variance: float):
        self.mean = mean
        self.variance = variance


class ModelWithGaussian(FromParams):
    def __init__(self, gaussian: Gaussian):
        self.gaussian = gaussian


param_str = """{"gaussian": {"mean": 0.0, "variance": 1.0}}"""
params = Params(json.loads(param_str))
model = ModelWithGaussian.from_params(params)
print(model)
