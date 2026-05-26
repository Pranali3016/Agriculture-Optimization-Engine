"""
train_model.py - Run this to retrain the model on your dataset.
Usage: python train_model.py
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'Crop_recommendation.csv')

print("📂 Loading dataset...")
df = pd.read_csv(DATA_PATH)
print(f"   Shape: {df.shape}")
print(f"   Crops: {df['label'].nunique()} unique crops")

X = df.drop('label', axis=1)
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\n🔧 Scaling features...")
scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc = scaler.transform(X_test)

print("🌲 Training Random Forest model...")
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train_sc, y_train)

y_pred = model.predict(X_test_sc)
acc = accuracy_score(y_test, y_pred)
print(f"\n✅ Accuracy: {acc * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\n💾 Saving model and scaler...")
joblib.dump(model, os.path.join(BASE_DIR, 'model.pkl'))
joblib.dump(scaler, os.path.join(BASE_DIR, 'scaler.pkl'))

print("📊 Saving crop statistics...")
stats = {}
for crop in df['label'].unique():
    crop_df = df[df['label'] == crop]
    stats[crop] = {}
    for col in ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']:
        stats[crop][col] = {
            'min': round(float(crop_df[col].min()), 1),
            'max': round(float(crop_df[col].max()), 1),
            'avg': round(float(crop_df[col].mean()), 1)
        }

with open(os.path.join(BASE_DIR, 'crop_stats.json'), 'w') as f:
    json.dump(stats, f, indent=2)

print("\n🎉 Training complete! Files saved:")
print("   - model.pkl")
print("   - scaler.pkl")
print("   - crop_stats.json")
