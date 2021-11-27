from allennlp.data.dataset_readers import DatasetReader
from allennlp.data.token_indexers import TokenIndexer, SingleIdTokenIndexer
from allennlp.data.instance import Instance
from allennlp.data.fields import TextField, LabelField
from allennlp.data.tokenizers import Token
from allennlp.data.vocabulary import Vocabulary
from allennlp.data.data_loaders import MultiProcessDataLoader
from allennlp.data.samplers.bucket_batch_sampler import BucketBatchSampler
from typing import Dict


class MyDatasetReader(DatasetReader):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._token_indexers: Dict[str, TokenIndexer] = {
            "id": SingleIdTokenIndexer(namespace="nt")
        }

    def _read(self, file_path):
        for tokens, label in zip(
            [["a", "b", "c", "d"], ["e"], ["f", "g", "h"], ["i", "j"]],
                ["a", "b", "c", "d"]):
            # zip函数返回一个元组迭代器，第i个元素的值由两个可迭代对象的第i个元素组成
            # result: {(['a', 'b', 'c', 'd'], 'a'), (['e'], 'b'), (['f', 'g', 'h'], 'c'), (['i', 'j'], 'd')}
            tokens = [Token(t) for t in tokens]
            text_field = TextField(tokens, self._token_indexers)
            label_field = LabelField(label)
            fields = {"t_tokens": text_field, "t_label": label_field}
            yield Instance(fields)


reader = MyDatasetReader()
vocab = Vocabulary.from_instances(reader.read("path_to_data"))
print(vocab.get_index_to_token_vocabulary(namespace="nt"))
print(vocab.get_index_to_token_vocabulary(namespace="labels"))

print("Default:")
data_loader = MultiProcessDataLoader(reader, "path_to_data", batch_size=3)
data_loader.index_with(vocab)

for batch in data_loader:
    print(batch)

print("Shuffle, and drop last batch if incomplete:")
data_loader = MultiProcessDataLoader(reader, "path_to_data",
                                     batch_size=3, shuffle=True, drop_last=True)
data_loader.index_with(vocab)
for batch in data_loader:
    print(batch)

print("Using the BucketBatchSampler:")
data_loader = MultiProcessDataLoader(
    reader, "path_to_data",
    batch_sampler=BucketBatchSampler(batch_size=3)
)

data_loader.index_with(vocab)
for batch in data_loader:
    print(batch)
