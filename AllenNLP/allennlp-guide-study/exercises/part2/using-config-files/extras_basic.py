import json

from allennlp.common import FromParams, Params
from allennlp.common.checks import ConfigurationError
# ConfigurationError: The exception raised by any AllenNLP object when it's misconfigured
# e.g. missing properties, invalid properties, unknown properties
from allennlp.data import Vocabulary


class Gaussian(FromParams):
    def __init__(self, mean: float, variance: float):
        self.mean = mean
        self.variance = variance


class ModelWithGaussian(FromParams):
    def __init__(self, vocab: Vocabulary, gaussian: Gaussian):
        self.vocab = vocab
        self.gaussian = gaussian
        print(f"ModelWithGaussian got vocab: {vocab}")


param_str = """{"gaussian": {"mean": 0.0, "variance": 1.0}}"""
params = Params(json.loads(param_str))
try:
    model = ModelWithGaussian.from_params(params)
except ConfigurationError:
    print("Caught ConfigurationError")

vocab = Vocabulary()
model = ModelWithGaussian.from_params(params=params, vocab=vocab)

