import os
import pickle
import pandas as pd
from flask import Flask, request, jsonify, render_template

from locations import location_names

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '..', 'ml_core', 'final_production_model.pkl')

if not os.path.exists(MODEL_PATH):
    print(f"CRITICAL ERROR: Model file not found at: {MODEL_PATH}")
    exit()

with open(MODEL_PATH, 'rb') as f:
    loaded_model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

@app.route('/get_locations', methods=['GET'])
def get_locations():
    return jsonify({'status': 'success', 'locations': location_names})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = pd.DataFrame([{
            'Total_Sq.ft': float(data['total_sqft']),
            'BHK': float(data['bhk']),
            'Location': data['location']
        }])

        prediction = loaded_model.predict(features)[0]
        return jsonify({'status': 'success', 'estimated_price_crores': prediction})
    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5000)