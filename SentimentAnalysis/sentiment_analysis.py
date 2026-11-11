"""Sentiment analyzer module"""

import json
import requests

API_BASE_URL = "https://sn-watson-sentiment-bert.labs.skills.network"
API_URL = API_BASE_URL + "/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"

def sentiment_analyzer(text: str) -> str:
    """
    This function analyzes a text.
    """
    response: requests.Response = requests.post(
        url=API_URL,
        headers={
            "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
        },
        json={ "raw_document": { "text": text} },
        timeout=500
    )

    label: str | None
    score: float | None
    if response.status_code == 200:
        formatted_response: dict = json.loads(response.text)
        label = formatted_response["documentSentiment"]["label"]
        score = formatted_response["documentSentiment"]["score"]
    else:
        label = None
        score = None

    return {"label": label, "score": score}
