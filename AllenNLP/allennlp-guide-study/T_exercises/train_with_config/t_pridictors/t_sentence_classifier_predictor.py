# 作 者：田宗林
# 时 间：2021/10/7
from allennlp.predictors import Predictor
from allennlp.common.util import JsonDict
from allennlp.data.instance import Instance


@Predictor.register("t_sentence_classifier")
class TemmSentenceClassifierPredictor(Predictor):
    def predict(self, text: str) -> JsonDict:
        inputs = {"text": text}
        return self.predict_json(inputs)

    def _json_to_instance(self, json_dict: JsonDict) -> Instance:
        text = json_dict["text"]
        return self._dataset_reader.text_to_instance(text)
