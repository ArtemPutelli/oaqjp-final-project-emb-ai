""" This is server file """
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def server():
    """ This is function """
    return render_template("index.html")

@app.route("/emotionDetector")
def server_emotion_detector():
    """ This is function """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        result = "Invalid text! Please try again!"
    else:
        result = f"""
        For the given statement, the system response is 'anger': {response["anger"]},
        'disgust': {response["disgust"]}, 'fear': {response["fear"]}, 'joy': {response["joy"]} and 'sadness': {response["sadness"]}.
        The dominant emotion is {response["dominant_emotion"]}.
        """
    return result

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
