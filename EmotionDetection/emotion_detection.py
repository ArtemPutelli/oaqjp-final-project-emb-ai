import requests
import json

def emotion_detector(text_to_analyze):
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    objct = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=headers, json=objct)

    response_json = json.loads(response.text)
    emotions = response_json["emotionPredictions"][0]["emotion"]

    result = {}

    dominant_emotion_key = ""
    dominant_emotion_value = 0

    for emotion in emotions:
        
        result[emotion] = emotions[emotion]
        
        if dominant_emotion_value < emotions[emotion]:
            dominant_emotion_key = emotion
            dominant_emotion_value = emotions[emotion]

    result["dominant_emotion"] = dominant_emotion_key

    return result