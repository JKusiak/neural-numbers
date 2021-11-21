import os
from flask import Flask, render_template, Response, request
from flask.templating import render_template
from repo import ClassifierRepo
from services import PredictDigitService
from settings import CLASSIFIER_STORAGE
from services import PredictDigitService
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def prediction():
    print('start prediction')
    repo = ClassifierRepo(CLASSIFIER_STORAGE)
    service = PredictDigitService(repo)
    image_data_uri = request.json['image']
    prediction = service.handle(image_data_uri)
    print(f'response is {prediction}')
    return Response(str(prediction).encode(), status=200)


if __name__ == 'main':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)