import os
import requests


NLP_URL = os.environ.get("NLP_URL", "nlp-url")
NLP_API_KEY = os.environ.get("NLP_API_KEY", "nlp-api")

TRAIN_SENTIMENT_ENDPOINT = "/v1/models/sentiment"
VERSION_PARAMETER = "?version=2021-03-25"


def train_sentiment_model(filepath):
    data = {
        "name": "Sentiment Gaia",
        "language": "en",
        "description": "Custom sentiment model for environment issues",
        "model_version": "0.1.0",
        "version": "2021-03-25"
    }
    files = {
        "training_data": (filepath, open(filepath, 'r', encoding="utf-8"),'text/csv')
    }

    url = NLP_URL + TRAIN_SENTIMENT_ENDPOINT + VERSION_PARAMETER
    res = requests.post(url,
                        data=data,
                        files=files,
                        auth=("apikey", NLP_API_KEY))

    res_json = res.json()
    model_id = res_json['model_id']
    return model_id


def get_model_status(model_id):
    url = f"{NLP_URL}{TRAIN_SENTIMENT_ENDPOINT}/{model_id}{VERSION_PARAMETER}"
    res = requests.get(url, auth=("apikey", NLP_API_KEY))

    return res


def delete_model(model_id):
    url = f"{NLP_URL}{TRAIN_SENTIMENT_ENDPOINT}/{model_id}{VERSION_PARAMETER}"
    res = requests.delete(url, auth=("apikey", NLP_API_KEY))
    
    return res

# delete_model(model_id)
# model_id = train_sentiment_model("D:/projects/Gaia/data/train2utf.csv")
# get_model_status(model_id)
