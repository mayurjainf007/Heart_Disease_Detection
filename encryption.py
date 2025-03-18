import os
import json
from cryptography.fernet import Fernet
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

KEY_PATH = 'encryption_key.key'

def load_or_generate_key():
    if not os.path.exists(KEY_PATH):
        key = Fernet.generate_key()
        with open(KEY_PATH, 'wb') as key_file:
            key_file.write(key)
        logging.info("Encryption key generated and saved")
    else:
        with open(KEY_PATH, 'rb') as key_file:
            key = key_file.read()
        logging.info("Encryption key loaded")
    return key

cipher = Fernet(load_or_generate_key())

def encrypt_data(data):
    return cipher.encrypt(json.dumps(data).encode()).decode()

def decrypt_data(data):
    return json.loads(cipher.decrypt(data.encode()).decode())
