# 作 者：田宗林
# 时 间：2021/10/5
from typing import Dict, Iterable
from allennlp.data.dataset_readers import DatasetReader
from allennlp.data.tokenizers import Tokenizer, WhitespaceTokenizer
from allennlp.data.token_indexers import TokenIndexer, SingleIdTokenIndexer
from allennlp.data.instance import Instance
from allennlp.data.fields import TextField, LabelField


@DatasetReader.register("t_classification-tsv")
class TemmClassficicationTsvReader(DatasetReader):
    def __init__(
            self,
            tokenizer: Tokenizer = None,
            token_indexers: Dict[str, TokenIndexer] = None,
            max_tokens: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.tokenizer = tokenizer or WhitespaceTokenizer()
        self.token_indexers = token_indexers or {"token_id": SingleIdTokenIndexer()}
        self.max_tokens = max_tokens

    def text_to_instance(self, text: str, label: str = None) -> Instance:
        tokens = self.tokenizer.tokenize(text)
        if self.max_tokens:
            tokens = tokens[: self.max_tokens]  # 预测时保持max_tokens一致，故"上移"
        text_field = TextField(tokens, self.token_indexers)
        fields = {"text": text_field}
        if label:
            fields["label"] = LabelField(label)

        return Instance(fields)

    def _read(self, file_path: str) -> Iterable[Instance]:
        with open(file_path, "r") as lines:
            for line in lines:
                text, label = line.strip().split("\t")
                yield self.text_to_instance(text, label)
