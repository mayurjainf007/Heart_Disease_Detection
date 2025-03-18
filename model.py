import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def train_model():
    data = pd.read_csv('heart_disease_data.csv')
    data.fillna(data.mean(), inplace=True)
    X = data.drop(columns=['target'])
    y = data['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    logging.info(f'Model Accuracy: {accuracy * 100:.2f}%')
    
    joblib.dump(model, 'heart_disease_model.pkl')
    logging.info("Model trained and saved successfully")

def load_model():
    return joblib.load('heart_disease_model.pkl')
