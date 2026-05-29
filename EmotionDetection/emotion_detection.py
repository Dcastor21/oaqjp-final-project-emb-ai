import requests
import json


def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    myobj = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=myobj, headers=headers)
    formatted_response =json.loads(response.text)
    emotion_predictions = formatted_response["emotionPredictions"][0]["emotion"]
    anger = emotion_predictions["anger"]
    disgust = emotion_predictions["disgust"]
    fear = emotion_predictions["fear"]
    joy = emotion_predictions["joy"]
    sadness = emotion_predictions["sadness"]

    emotions_dict = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
    }

    
    dominant_emotion = max(emotions_dict, key=emotions_dict.get)

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion,
    }


    