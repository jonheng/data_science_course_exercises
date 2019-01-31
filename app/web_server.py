from flask import Flask, jsonify, request
import os, joblib
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify("hello data science")

@app.route('/predict', methods=['POST'])
def predict():
    request_payload = request.json
    # TODO: transform payload and return result of model.predict()

    return jsonify({'predicted price (thousands)': 'TODO'})

if __name__ == '__main__':
    # TODO: load artifacts from disk
    
    app.run(port=8080, host='0.0.0.0', debug=True)