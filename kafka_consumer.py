from kafka import KafkaConsumer
import json
import numpy as np
import joblib
from encryption import decrypt_data

# Load trained model
model = joblib.load("heart_disease_model.pkl")

consumer = KafkaConsumer(
    'patient_data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    data = message.value
    decrypted_data = decrypt_data(data)
    features = np.array([decrypted_data['heart_rate'], decrypted_data['blood_pressure'], decrypted_data['oxygen_saturation']]).reshape(1, -1)
    prediction = model.predict(features)
    print(f"Real-time Prediction: {prediction}")
