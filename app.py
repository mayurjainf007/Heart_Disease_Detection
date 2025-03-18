import os
import logging
import json
import numpy as np
import joblib
from flask import Flask, request, jsonify
from database import get_db_connection
from model import train_model, load_model
from encryption import encrypt_data, decrypt_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        encrypted_data = request.json['data']
        decrypted_data = decrypt_data(encrypted_data)
        input_data = np.array(decrypted_data).reshape(1, -1)
        model = load_model()
        prediction = model.predict(input_data)[0]
        return jsonify({'prediction': int(prediction)})
    except Exception as e:
        logging.error(f"Prediction error: {str(e)}")
        return jsonify({'error': 'Invalid input or server error'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
