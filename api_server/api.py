from fastapi import FastAPI

from dataset_service import load_dataset
from model_service import analyze_text

api = FastAPI()


@api.get("/predict_sentimental")
def predict_sentimental(message_text: str):
    return analyze_text(message_text)
    # return {"positive": "predict_sentimental", "neutral": "predict_sentimental", "negative": "predict_sentimental"}


@api.get("/get_dataset")
def get_dataset():
    dados = load_dataset()
    return dados


# @api.get("/get_all_predictions")
# def get_predictions():
#     all_predictions = data_handler.get_all_predictions()
#
#     return all_predictions
#
#
# @api.post("/save_prediction")
# def save_prediction(passageiro_json: Any = Body(None)):
#     passageiro = json.loads(passageiro_json)
#
#     result = data_handler.save_prediction(passageiro)
#
#     return result
#
#
# @api.post("/predict")
# def predict(passageiro_json: Any = Body(None)):
#     passageiro = json.loads(passageiro_json)
#
#     result = data_handler.survival_predictor(passageiro)
#
#     return result
