"""This file is for emotion detection"""

from flask import Flask, render_template, request
#importing included package
from EmotionDetection.emotion_detection import emotion_detector

#Start of application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """function printing emotions"""
    #this function will call to emotion_detector and analyze input text
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    #in case of no response included, error will occur
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"<b>{response['dominant_emotion']}</b>."
    )

@app.route("/")
def render_index_page():
    """function routing homepage"""
    return render_template('index.html')

#port
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
