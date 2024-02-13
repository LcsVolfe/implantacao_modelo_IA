import json


def get_all_predictions():
    data = None
    with open('predictions.json', 'r') as f:
        data = json.load(f)

    return data


def save_prediction(analise):
    data = get_all_predictions()
    data.append(analise)
    with open('predictions.json', 'w') as f:
        json.dump(data, f)
