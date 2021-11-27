# 作 者：田宗林
# 时 间：2021/9/26
from typing import Tuple, Optional
from allennlp.modules.seq2vec_encoders import Seq2VecEncoder
from allennlp.nn import Activation


@Seq2VecEncoder.register("sve")
class CnnEncoder(Seq2VecEncoder):
    def __init__(self,
        embedding_dim: int,
        num_filters: int,
        ngram_filter_sizes: Tuple[int],
        conv_layer_activations: Activation = None,
        output_dim: Optional[int] = None
        ) -> None:
        super().__init__()


print(Seq2VecEncoder.list_available())
print(Seq2VecEncoder.by_name('sve'))
print(Seq2VecEncoder.by_name('cnn'))
