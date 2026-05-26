from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import json
import os

app = Flask(__name__)
CORS(app)

# Load model and scaler
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, 'model.pkl'))
scaler = joblib.load(os.path.join(BASE_DIR, 'scaler.pkl'))

with open(os.path.join(BASE_DIR, 'crop_stats.json')) as f:
    crop_stats = json.load(f)

CROP_EMOJIS = {
    'rice': '🌾', 'maize': '🌽', 'chickpea': '🫘', 'kidneybeans': '🫘',
    'pigeonpeas': '🫛', 'mothbeans': '🫘', 'mungbean': '🫘', 'blackgram': '🖤',
    'lentil': '🫘', 'pomegranate': '🍎', 'banana': '🍌', 'mango': '🥭',
    'grapes': '🍇', 'watermelon': '🍉', 'muskmelon': '🍈', 'apple': '🍎',
    'orange': '🍊', 'papaya': '🫐', 'coconut': '🥥', 'cotton': '🌿',
    'jute': '🌿', 'coffee': '☕'
}

CROP_TIPS = {
    'rice': 'Best grown in flooded paddies. Requires standing water during growth phase.',
    'maize': 'Requires well-drained soil. Sensitive to waterlogging.',
    'chickpea': 'Drought-tolerant legume. Fixes atmospheric nitrogen.',
    'kidneybeans': 'Grows best in loamy soil with good drainage.',
    'pigeonpeas': 'Highly drought-resistant. Great for intercropping.',
    'mothbeans': 'Very hardy crop. Thrives in arid conditions.',
    'mungbean': 'Short duration crop. Great for crop rotation.',
    'blackgram': 'Nitrogen-fixing legume. Improves soil fertility.',
    'lentil': 'Cool-season crop. Fixes nitrogen in the soil.',
    'pomegranate': 'Drought tolerant fruit. Requires warm climate.',
    'banana': 'Needs high humidity and warmth. Rich in potassium.',
    'mango': 'Tropical tree fruit. Requires dry spell before flowering.',
    'grapes': 'Requires well-drained soil and cool winters.',
    'watermelon': 'Needs long warm growing season and sandy soil.',
    'muskmelon': 'Similar to watermelon. Needs warm temperatures.',
    'apple': 'Requires cold winters for dormancy. High altitude preferred.',
    'orange': 'Subtropical citrus. Needs frost-free climate.',
    'papaya': 'Fast-growing tropical fruit. Very sensitive to frost.',
    'coconut': 'Coastal tropical palm. Thrives near sea level.',
    'cotton': 'Warm season crop. Requires 6+ months frost-free.',
    'jute': 'Grows in warm humid climate. Needs heavy rainfall.',
    'coffee': 'Shade-loving crop. Grows best at high altitudes.'
}


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'message': 'Crop Recommendation API is running'})


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        required = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

        for field in required:
            if field not in data:
                return jsonify({'error': f'Missing field: {field}'}), 400

        features = np.array([[
            float(data['N']),
            float(data['P']),
            float(data['K']),
            float(data['temperature']),
            float(data['humidity']),
            float(data['ph']),
            float(data['rainfall'])
        ]])

        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]
        probabilities = model.predict_proba(features_scaled)[0]
        classes = model.classes_

        # Top 3 predictions
        top3_idx = np.argsort(probabilities)[-3:][::-1]
        top3 = [
            {
                'crop': classes[i],
                'emoji': CROP_EMOJIS.get(classes[i], '🌱'),
                'confidence': round(float(probabilities[i]) * 100, 1)
            }
            for i in top3_idx
        ]

        return jsonify({
            'prediction': prediction,
            'emoji': CROP_EMOJIS.get(prediction, '🌱'),
            'confidence': round(float(max(probabilities)) * 100, 1),
            'tip': CROP_TIPS.get(prediction, 'Ensure proper soil preparation and irrigation.'),
            'top3': top3,
            'stats': crop_stats.get(prediction, {})
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/crops', methods=['GET'])
def get_crops():
    crops = [
        {
            'name': crop,
            'emoji': CROP_EMOJIS.get(crop, '🌱'),
            'stats': crop_stats.get(crop, {})
        }
        for crop in sorted(crop_stats.keys())
    ]
    return jsonify({'crops': crops})


@app.route('/crop/<crop_name>', methods=['GET'])
def get_crop_detail(crop_name):
    if crop_name not in crop_stats:
        return jsonify({'error': 'Crop not found'}), 404
    return jsonify({
        'name': crop_name,
        'emoji': CROP_EMOJIS.get(crop_name, '🌱'),
        'tip': CROP_TIPS.get(crop_name, ''),
        'stats': crop_stats[crop_name]
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
