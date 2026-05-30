from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
 
app = Flask(__name__)
 

@app.route("/") 
def render_index_page(): 
    return render_template('index.html')


 
@app.route("/emotionDetector")
def emotion_detector_route():
    
    text_to_analyse = request.args.get("textToAnalyze")
 
    
    if not text_to_analyse.strip():
        return "Invalid text! Please try again.", 400
 
    result = emotion_detector(text_to_analyse)
 
    
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again.", 400
 
    anger   = result["anger"]
    disgust = result["disgust"]
    fear    = result["fear"]
    joy     = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]
 
    
    output = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )
 
    return output
 
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
 