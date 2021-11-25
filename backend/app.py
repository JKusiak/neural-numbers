import os
from flask import Flask, render_template, Response, request
from flask.templating import render_template
from fetch_classifier import FetchStoredClassifier
from digit_prediction import PredictDigitService
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BASE_DIR = os.getcwd()
STORAGE_PATH = os.path.join(BASE_DIR, 'storage/classifier.txt')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def prediction():
    image_data_uri = request.json['image']
    classifier = FetchStoredClassifier(STORAGE_PATH)
    service = PredictDigitService(classifier)
    prediction = service.predict(image_data_uri)
    return Response(str(prediction).encode(), status=200)


if __name__ == 'main':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)