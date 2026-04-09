import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "large_health_dataset.csv"
if not DATA_PATH.exists():
    raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")
df = pd.read_csv(str(DATA_PATH))
df = df.dropna()
le_gender = LabelEncoder()
df['gender'] = le_gender.fit_transform(df['gender'])
le_activity = LabelEncoder()
df['physical_activity_level'] = le_activity.fit_transform(df['physical_activity_level'])
le_disease = LabelEncoder()
df['disease_name'] = le_disease.fit_transform(df['disease_name'])
X = df.drop('disease_name', axis=1)
y = df['disease_name']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_reshaped = X_scaled.reshape((X_scaled.shape[0], 1, X_scaled.shape[1]))
X_train, X_test, y_train, y_test = train_test_split(X_reshaped, y, test_size=0.2, random_state=42)
model = Sequential([
    LSTM(64, input_shape=(1, X.shape[1]), return_sequences=True),
    Dropout(0.2),
    LSTM(32),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dense(len(le_disease.classes_), activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print("Starting training...")
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1, verbose=1)
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy:.4f}")
SAVE_DIR = BASE_DIR / "Prediction_App" / "ml_models"
if not SAVE_DIR.exists():
    SAVE_DIR.mkdir(parents=True, exist_ok=True)
model.save(str(SAVE_DIR / 'health_model.h5'))
with open(SAVE_DIR / 'scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
with open(SAVE_DIR / 'le_gender.pkl', 'wb') as f:
    pickle.dump(le_gender, f)
with open(SAVE_DIR / 'le_activity.pkl', 'wb') as f:
    pickle.dump(le_activity, f)
with open(SAVE_DIR / 'le_disease.pkl', 'wb') as f:
    pickle.dump(le_disease, f)
print(f"Model and artifacts saved successfully to {SAVE_DIR}!")
