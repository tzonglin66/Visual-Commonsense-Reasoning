from allennlp.data import DatasetReader, Instance
from allennlp.data.tokenizers import Tokenizer, WhitespaceTokenizer
from allennlp.data.token_indexers import TokenIndexer, SingleIdTokenIndexer
from allennlp.data.fields import Field, LabelField, TextField
from typing import Dict, Iterable


@DatasetReader.register("classification-tsv")
class ClassificationTsvReader(DatasetReader):
    def __init__(self,
                 tokenizer: Tokenizer = None,
                 token_indexers: Dict[str, TokenIndexer] = None,
                 max_tokens: int = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.tokenizer = tokenizer or WhitespaceTokenizer()
        self.token_indexers = token_indexers or {"tokens": SingleIdTokenIndexer()}
        self.max_tokens = max_tokens

    def text_to_instance(self,
                         text: str,
                         label: str = None) -> Instance:
        tokens = self.tokenizer.tokenize(text)
        if self.max_tokens:
            tokens = tokens[:self.max_tokens]
        text_field = TextField(tokens, self.token_indexers)
        fields: Dict[str, Field] = {"text": text_field}
        if label:
            fields["label"] = LabelField(label)
        return Instance(fields)

    def _read(self, file_path: str) -> Iterable[Instance]:
        with open(file_path, "r") as lines:
            for line in lines:
                text, sentiment = line.strip().split("\t")
                yield self.text_to_instance(text=text, label=sentiment)


reader = ClassificationTsvReader()
dataset = list(reader.read("E:\\root\\Projects\\learn_nlp\\quick_start\\data\\movie_review\\train.tsv"))

print("type of its first element: ", type(dataset[0]))
# print("value of its first element: ", dataset[0])
print("size of dataset: ", len(dataset))
