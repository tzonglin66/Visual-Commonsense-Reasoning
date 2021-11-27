# 作 者：田宗林
# 时 间：2021/9/26
from allennlp.common import FromParams
from allennlp.common import Params
import json

class Gaussian(FromParams):
    def __init__(self, mean: float, variance: float):
        self.mean = mean
        self.variance = variance


param_str = """{"mean": 0.0, "variance": 1.0}"""
params = Params(json.loads(param_str))
gaussian = Gaussian.from_params(params)
