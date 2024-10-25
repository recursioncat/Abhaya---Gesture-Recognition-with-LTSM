from flask import Flask, request, jsonify
import numpy as np
from dependencies import *
import keras
import os

app = Flask(__name__)
model = keras.models.load_model('VideoRecognitionV2_Bekar.keras')
classes = ['Are you free today', 'Can you repeat that please',
       'Congratulations', 'help me please', 'how are you', 'I am fine',
       'I love you', 'no', 'Please come,Welcome', 'Talk slower please',
       'Thank You', 'What are you doing', 'What do you do',
       'What Happened', 'yes']

def preProcessVideo(url):
    vid = extractPostitionFromVideo(url)
    vid = np.array([vid])
    return vid
    

@app.route('/predictfromvideo', methods=['POST', 'GET'])
def predict():
     data = request.get_json(force=True)
     url = data['url']
     video = preProcessVideo(url)
     
     result = model.predict(video)
     results = classes[np.argmax(result)]
     print(result)
     print("Confidence: ", np.max(result)*100)
     
     return jsonify(results)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 