import torch
from allennlp.common import FromParams
from allennlp.nn.activations import Activation
from typing import List, Union

class FeedForward(torch.nn.Module, FromParams):

    def __init__(
        self,
        input_dim: int,
        num_layers: int,
        hidden_dims: Union[int, List[int]],
        activations: Union[Activation, List[Activation]],
        dropout: Union[float, List[float]] = 0.0,
        ) -> None:
        super().__init__()
