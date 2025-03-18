from kafka import KafkaProducer, KafkaConsumer
import json
import time
import random

# Kafka Producer (Simulates IoT Health Devices)
def generate_patient_data():
    return {
        "heart_rate": random.randint(60, 120),
        "blood_pressure": random.randint(80, 140),
        "oxygen_saturation": random.uniform(90, 100)
    }

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = generate_patient_data()
    producer.send('patient_vitals', value=data)
    print(f"Sent: {data}")
    time.sleep(5)
