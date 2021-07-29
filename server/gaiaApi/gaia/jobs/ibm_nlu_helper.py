"""
    File containing helper functions related to IBM NLU API
    
    Maintainers:
    - kaniaprameswara5@gmail.com
"""

import os
import json
import logging
import requests

from pathlib import Path
from typing import Dict, List
from dataclasses import asdict

import nltk

from gaia.enum.sentiment import SentimentHelper
from gaia.dataclass.document import Document

NLP_URL = os.environ.get("NLP_URL", "nlp-url")
NLP_API_KEY = os.environ.get("NLP_API_KEY", "nlp-key")
SENTIMENT_MODEL_ID = os.environ.get("SENTIMENT_MODEL_ID", "model-id")

ANALYZE_ENDPOINT = "/v1/analyze?version=2021-03-25"
TRAIN_SENTIMENT_ENDPOINT = "/v1/models/sentiment"

BRAND_ENTITY_SUBTYPES = ["Brand", "Company"]


def get_documents(filepath: Path) -> List[Document]:
    docs = []
    with open(filepath) as f:
        docs_json = json.load(f)
        docs = [Document(**d) for d in docs_json]

    return docs


def sanitize_article(article: str) -> str:
    return article.replace("\\u201c", '"') \
                  .replace("\\u201d", '"') \
                  .replace("\\u2019", "'")


def is_brand_entity(entity: Dict) -> bool:
    entity_subtypes = entity.get("disambiguation", dict()).get("subtype")
    if entity_subtypes is not None:
        return any([s for s in entity_subtypes if s in BRAND_ENTITY_SUBTYPES])
    return False


def analyze_ibm_entity_sentiment(doc: Document) -> Document:
    text_per_sentence = nltk.sent_tokenize(doc.article)
    overall_sentiment = {}

    analyze_url = "{}{}".format(NLP_URL, ANALYZE_ENDPOINT)
    headers = {
        "Content-Type": "application/json"
    }

    for sentence in text_per_sentence:
        data = {
            "text": sentence,
            "language": "en",
            "features": {
                "sentiment": {
                    "model": SENTIMENT_MODEL_ID,
                    "document": True
                },
                "entities": {
                    "sentiment": True
                },
                "keywords": {
                    "sentiment": True
                }
            }                    
        }

        res = requests.post(analyze_url,
                            data=json.dumps(data),
                            headers=headers,
                            auth=("apikey", NLP_API_KEY))
        res_json = res.json()

        entities = res_json["entities"]
        brand_entities = [e for e in entities if is_brand_entity(e)]
        doc.brand_entities.extend(brand_entities)
        for entity in brand_entities:
            entity_name = entity["text"]
            sentiment = entity["sentiment"]
            score = sentiment["score"]
            label = sentiment["label"]

            if entity_name not in overall_sentiment:
                overall_sentiment[entity_name] = {"score": 0, "label": 0}
            overall_sentiment[entity_name]["score"] += score
            overall_sentiment[entity_name]["label"] += SentimentHelper.encode_sentiment(label)

    for brand in overall_sentiment.keys():
        label = overall_sentiment[brand]["label"]
        overall_sentiment[brand]["label"] = SentimentHelper.decode_sentiment(label)

    doc.sentiment = overall_sentiment

    return doc


def analyze_entity_sentiment(filepath: Path) -> List[Dict]:
    docs = get_documents(filepath)

    for doc in docs:
        try:
            doc.article = sanitize_article(doc.article)
            doc = analyze_ibm_entity_sentiment(doc)
        except Exception as e:
            logging.exception("Err:", e)

    docs = [d for d in docs if len(d.brand_entities) > 0]
    return docs

    # with open(output, "w") as f:
    #     json.dump(docs_dict, f)
