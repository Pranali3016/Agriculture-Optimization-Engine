<div align="center">

# 🌱 CropSense — Agriculture Production Optimization Engine

**An end-to-end Machine Learning web app that recommends the best crop based on soil & climate conditions**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Accuracy](https://img.shields.io/badge/Model%20Accuracy-99.32%25-2d6a4f?style=for-the-badge)](/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

[🌐 Live Demo](https://Pranali3016.github.io/Agriculture-Optimization-Engine) · [📡 API](https://crop-recommendation-api.onrender.com) · [📓 Notebook](notebooks/Agriculture_Production_Optimization_Engine.ipynb)

</div>

---

## 📌 Overview

CropSense takes **7 soil and climate measurements** from your field and instantly recommends the best crop to grow using a **Random Forest ML model** trained on 2200 samples across 22 crop types — achieving **99.32% test accuracy**.

Built as a complete end-to-end project:
- 🧠 **ML Backend** — scikit-learn Random Forest via Flask REST API  
- 🌐 **Web Frontend** — beautiful single-page app, no framework needed  
- ☁️ **Fully Deployed** — GitHub Pages (frontend) + Render (API)  
- 🔄 **CI/CD** — GitHub Actions auto-deploys on every push  

---

## 🖼 Screenshots

| Home Page | Prediction Result |
|-----------|-------------------|
| ![Home](assets/screenshot-home.png) | ![Result](assets/screenshot-result.png) |

> **Try sample inputs:** Click "Try rice conditions" or "Try mango" on the website — it auto-fills all fields!

---

## 🏗 System Architecture

```
┌─────────────────┐     POST /predict      ┌──────────────────┐     predict()    ┌─────────────────┐
│   User Browser  │ ──────────────────────▶ │   Flask API      │ ───────────────▶ │  Random Forest  │
│  (index.html)   │                         │   (app.py)       │                  │  (model.pkl)    │
│                 │ ◀────────────────────── │  validates +     │ ◀─────────────── │  100 trees      │
│  N,P,K,Temp,    │   JSON: crop+confidence │  scales inputs   │  crop + proba    │  99.32% acc.    │
│  Humidity,pH,   │                         │                  │                  │                 │
│  Rainfall       │                         │                  │                  │  scaler.pkl     │
└─────────────────┘                         └──────────────────┘                  └─────────────────┘

Training Pipeline:
Crop_recommendation.csv (2200 rows)
        │
        ▼
StandardScaler → train_test_split(80/20) → RandomForestClassifier(n_estimators=100)
        │
        ▼
model.pkl + scaler.pkl  →  Accuracy: 99.32%

Deployment:
GitHub Pages (frontend)  +  Render.com (Flask API)  +  GitHub Actions (CI/CD)
```

---

## 📊 Input Parameters

| Parameter | Unit | Description | Typical Range |
|-----------|------|-------------|---------------|
| **N** | kg/ha | Nitrogen content in soil | 0 – 140 |
| **P** | kg/ha | Phosphorus content in soil | 5 – 145 |
| **K** | kg/ha | Potassium content in soil | 5 – 205 |
| **Temperature** | °C | Average ambient temperature | 8 – 43 |
| **Humidity** | % | Relative humidity | 14 – 100 |
| **pH** | 0–14 | Soil acidity/alkalinity | 3.5 – 9.9 |
| **Rainfall** | mm | Average annual rainfall | 20 – 300 |

---

## 🌾 Supported Crops (22)

| Category | Crops |
|----------|-------|
| 🌾 **Cereals** | Rice, Maize |
| 🫘 **Pulses / Legumes** | Chickpea, Kidney Beans, Pigeon Peas, Moth Beans, Mung Bean, Black Gram, Lentil |
| 🍎 **Fruits** | Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut |
| 🌿 **Cash Crops** | Cotton, Jute, Coffee |

---

## 🧠 ML Model Details

| Property | Value |
|----------|-------|
| Algorithm | Random Forest Classifier |
| No. of Trees | 100 |
| Feature Scaling | StandardScaler |
| Train / Test Split | 80% / 20% |
| **Test Accuracy** | **99.32%** |
| Output | Crop name + Confidence % + Top-3 alternatives |

### Why Random Forest?

- ✅ Handles non-linear relationships in agricultural data  
- ✅ Robust to outliers and noisy sensor readings  
- ✅ Built-in feature importance — shows which soil factor matters most  
- ✅ No assumptions about data distribution  
- ✅ Excellent generalization with minimal hyperparameter tuning  

### Model Performance

```
              precision    recall  f1-score   support
       apple       1.00      1.00      1.00        20
      banana       1.00      1.00      1.00        20
   blackgram       1.00      1.00      1.00        20
    chickpea       0.95      1.00      0.97        20
      coffee       1.00      1.00      1.00        20
      cotton       1.00      1.00      1.00        20
      grapes       1.00      1.00      1.00        20
        jute       1.00      0.95      0.97        20
  kidneybeans      1.00      1.00      1.00        20
       lentil      1.00      1.00      1.00        20
        maize       1.00      1.00      1.00        20
        mango       1.00      1.00      1.00        20
    mothbeans       1.00      1.00      1.00        20
     mungbean       1.00      1.00      1.00        20
     muskmelon      1.00      1.00      1.00        20
       orange       1.00      1.00      1.00        20
       papaya       1.00      1.00      1.00        20
   pigeonpeas       1.00      1.00      1.00        20
  pomegranate       1.00      1.00      1.00        20
         rice       1.00      1.00      1.00        20
   watermelon       1.00      1.00      1.00        20

    accuracy                           0.9932       440
   macro avg        0.998     0.998    0.998        440
```

> ⚠️ **Overfitting Note:** The 99.32% accuracy looks impressive but should be interpreted with caution. The dataset is perfectly balanced (exactly 100 samples per crop) and follows clean, well-separated distributions — making classification easier than real-world conditions. The test set is drawn from the same synthetic distribution as training, so it does not represent true out-of-sample performance on messy field sensor data. The model has likely overfit this dataset. To improve generalization, consider k-fold cross-validation, collecting diverse real-world samples, or adding stronger regularization.

---

## 📁 Project Structure

```
crop-recommendation-app/
│
├── 📂 backend/
│   ├── app.py                    # Flask REST API (predict, crops, health endpoints)
│   ├── train_model.py            # Retrain the model anytime with new data
│   ├── Crop_recommendation.csv   # Training dataset (2200 rows × 8 columns)
│   ├── model.pkl                 # Pre-trained Random Forest model
│   ├── scaler.pkl                # Fitted StandardScaler
│   ├── crop_stats.json           # Per-crop optimal conditions
│   ├── requirements.txt          # Python dependencies
│   └── Dockerfile                # Docker container config
│
├── 📂 frontend/
│   └── index.html                # Complete single-page web app (HTML + CSS + JS)
│
├── 📂 notebooks/
│   └── Agriculture_Production_Optimization_Engine.ipynb  # EDA + model exploration
│
├── 📂 .github/
│   └── workflows/
│       └── deploy.yml            # GitHub Actions — auto deploys frontend to Pages
│
├── README.md
├── LICENSE
├── .gitignore
└── upload_to_github.sh           # Step-by-step git upload helper script
```

---

## 🚀 Quick Start (Run Locally)

### Prerequisites
- Python 3.10+
- pip

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/crop-recommendation-app.git
cd crop-recommendation-app
```

### 2. Set up backend

```bash
cd backend
pip install -r requirements.txt
```

### 3. (Optional) Retrain the model

```bash
python train_model.py
```

### 4. Start the Flask API

```bash
python app.py
# ✅ Running on http://localhost:5000
```

### 5. Open the frontend

Open `frontend/index.html` in your browser — it connects to `localhost:5000` automatically.

---

## 🧪 Sample Test Inputs

| Crop | N | P | K | Temp | Humidity | pH | Rainfall |
|------|---|---|---|------|----------|----|----------|
| 🌾 Rice | 70 | 50 | 45 | 23 | 85 | 6.2 | 200 |
| 🌽 Maize | 70 | 60 | 25 | 22 | 65 | 6.0 | 75 |
| 🥭 Mango | 10 | 25 | 35 | 28 | 52 | 5.8 | 105 |
| ☕ Coffee | 10 | 25 | 35 | 26 | 65 | 6.2 | 200 |
| 🌿 Cotton | 120 | 50 | 20 | 25 | 80 | 6.8 | 88 |
| 🍎 Apple | 10 | 135 | 210 | 20 | 92 | 6.0 | 130 |
| 🍌 Banana | 85 | 70 | 55 | 26 | 80 | 6.5 | 105 |
| 🍇 Grapes | 10 | 120 | 200 | 14 | 87 | 6.2 | 67 |

---

## 📡 API Reference

**Base URL (local):** `http://localhost:5000`  
**Base URL (production):** `https://crop-recommendation-api.onrender.com`

### `POST /predict` — Get crop recommendation

**Request body:**
```json
{
  "N": 70,
  "P": 50,
  "K": 45,
  "temperature": 23,
  "humidity": 85,
  "ph": 6.2,
  "rainfall": 200
}
```

**Response:**
```json
{
  "prediction": "rice",
  "emoji": "🌾",
  "confidence": 99.0,
  "tip": "Best grown in flooded paddies. Requires standing water during growth phase.",
  "top3": [
    { "crop": "rice",    "emoji": "🌾", "confidence": 99.0 },
    { "crop": "jute",    "emoji": "🌿", "confidence": 0.7  },
    { "crop": "coconut", "emoji": "🥥", "confidence": 0.3  }
  ],
  "stats": {
    "N":           { "min": 60.0, "max": 80.0, "avg": 70.1 },
    "P":           { "min": 40.0, "max": 60.0, "avg": 50.2 },
    "K":           { "min": 40.0, "max": 50.0, "avg": 45.1 },
    "temperature": { "min": 20.0, "max": 27.0, "avg": 23.5 },
    "humidity":    { "min": 80.0, "max": 90.0, "avg": 85.0 },
    "ph":          { "min": 5.5,  "max": 7.0,  "avg": 6.2  },
    "rainfall":    { "min": 150.0,"max": 250.0,"avg": 200.0 }
  }
}
```

### `GET /crops` — List all supported crops

```bash
curl http://localhost:5000/crops
```

### `GET /health` — Health check

```bash
curl http://localhost:5000/health
# {"status": "ok", "message": "Crop Recommendation API is running"}
```

---

## ☁️ Deployment Guide

### Backend → Render.com (Free Tier)

1. Push code to GitHub  
2. Go to [render.com](https://render.com) → **New → Web Service**  
3. Connect your GitHub repo  
4. Configure:

| Setting | Value |
|---------|-------|
| Root Directory | `backend` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |
| Instance Type | Free |

5. Click **Deploy** → copy the URL (e.g. `https://crop-api-xyz.onrender.com`)  
6. Update `API_BASE` in `frontend/index.html`:

```javascript
const API_BASE = 'https://crop-api-xyz.onrender.com';
```

### Frontend → GitHub Pages (Free)

1. Push to GitHub  
2. Repo **Settings → Pages → Source: GitHub Actions**  
3. The included `deploy.yml` auto-deploys `frontend/` on every push to `main`  
4. Your site: `https://YOUR_USERNAME.github.io/crop-recommendation-app`  

### Docker (Optional)

```bash
cd backend
docker build -t crop-api .
docker run -p 5000:5000 crop-api
```

---

## 🔧 Tech Stack

| Layer | Technology |
|-------|-----------|
| ML Model | scikit-learn · Random Forest · StandardScaler |
| API Server | Flask 3.0 · Flask-CORS · Gunicorn |
| Frontend | Vanilla HTML5 · CSS3 · JavaScript (no framework) |
| Containerization | Docker |
| Frontend Hosting | GitHub Pages |
| API Hosting | Render.com |
| CI/CD | GitHub Actions |
| Notebook | Jupyter · pandas · matplotlib · seaborn |

---

## 📓 Notebook Highlights

The [`notebooks/`](notebooks/) folder contains the original EDA and ML exploration:

- 📊 **Exploratory Data Analysis** — crop distribution, missing values, statistics per crop  
- 📈 **Interactive comparisons** — which crops need above/below average N, P, K  
- 🔍 **Pattern discovery** — summer crops, winter crops, rainy season crops  
- 📉 **KMeans clustering** — elbow method, 4-cluster analysis  
- 🤖 **Logistic Regression baseline** — confusion matrix, classification report  

---

## 👩‍💻 About the Author

**Pranali**  
B.E. — Artificial Intelligence & Data Science (2024)  
VPKBIET Baramati · CGPA: 8.19

- 📄 **IEEE Published** — Indian Sign Language Interpreter using LSTM (96.25% accuracy) — MITADTSoCiCon 2024  
- 💼 Ex-Associate Software Engineer @ Test Yantra (Python ML pipelines)  
- 🔭 Currently building: Generative AI · Agentic AI · LangGraph systems  

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

<div align="center">

⭐ **If this project helped you, please give it a star!** ⭐

Made with 🌱 by Pranali

</div>
