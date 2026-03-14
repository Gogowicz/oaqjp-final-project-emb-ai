import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    # URL of the Emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
     # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }  
    # Custom header specifying the model ID for the emotion dectector service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    # Sending a POST request to the emotion detector API
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    # set all values to none if status_code = 400
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    # Extracting sentiment label and score from the response
    anger= formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    # dictornary of the emotions
    emotion_scores = {
    "anger": anger,
    "disgust": disgust,
    "fear": fear,
    "joy": joy,
    "sadness": sadness
    }
    # getting key of emotion with maximum score
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    
    # Returning a dictionary containing sentiment analysis results
    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion}
    
