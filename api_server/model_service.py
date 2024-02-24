

import numpy as np

from scipy.special import softmax
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
from deep_translator import GoogleTranslator


MODEL_NAME = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
config = AutoConfig.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)


def analyze_text(text):
    if not text:
        return
    print(f"Texto entrada: {text}")
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    print(f"Texto saida: {translated}")
    encoded_input = tokenizer(translated, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    result = dict()
    for i in range(scores.shape[0]):
        l = config.id2label[ranking[i]]
        s = scores[ranking[i]]
        result[l] = np.round(float(s), 4)
    return result
