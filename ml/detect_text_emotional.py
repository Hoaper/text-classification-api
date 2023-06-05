from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from enum import Enum


class SupportedLangs(Enum):
    RU = "RU"
    ENG = "ENG"


class DetectTextEmotional:

    def __init__(self):
        # ENGLISH TOKENIZER/MODEL/LABELS
        self._tokenizer_eng = AutoTokenizer.from_pretrained("j-hartmann/emotion-english-distilroberta-base")
        self._model_eng = AutoModelForSequenceClassification.from_pretrained("j-hartmann/emotion-english-distilroberta-base")
        self._model_labels_eng = self._model_eng.config.id2label

        # RUSSIAN TOKENIZER/MODEL/LABELS
        self._tokenizer_ru = AutoTokenizer.from_pretrained("cointegrated/rubert-tiny2-cedr-emotion-detection")
        self._model_ru = AutoModelForSequenceClassification.from_pretrained("cointegrated/rubert-tiny2-cedr-emotion-detection")
        self._model_labels_ru = self._model_ru.config.id2label

    def _get_locale_tokenizer_model_label(self, lang: str):
        if lang == SupportedLangs.ENG.value:
            return self._tokenizer_eng, self._model_eng, self._model_labels_eng
        elif lang == SupportedLangs.RU.value:
            return self._tokenizer_ru, self._model_ru, self._model_labels_ru
        else:
            return None, None, None

    def get_result(self, text: str, lang: str):
        tokenizer, model, labels = self._get_locale_tokenizer_model_label(lang.upper())

        if not tokenizer:
            return "Incorrect data"

        inputs = tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            logits = model(**inputs).logits

        max_res = logits.argmax().item()
        out = {
            "full_result": {},
            "text": text if len(text) < 125 else text[:125] + "...",
            "better_result": {"label": labels[max_res], "score": round(logits[0][max_res].item(), 3)}
        }
        for _id, label in labels.items():
            out["full_result"][label] = round(logits[0][_id].item(), 3)

        return out

