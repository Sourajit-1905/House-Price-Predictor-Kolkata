import os
import pickle
import pandas as pd
from flask import Flask, request, jsonify, render_template

from locations import location_names

app = Flask(__name__)

PROJECT_ROOT = r"C:\Users\Biswajit\Desktop\SP49\AI & ML\Projects\Kolkata_House_Price_Predictor"
MODEL_PATH = os.path.join(PROJECT_ROOT, "ml_core", "final_production_model.pkl")
DATASET_PATH = os.path.join(PROJECT_ROOT, "data", "House_Price.csv")

if not os.path.exists(MODEL_PATH):
    print(f"CRITICAL ERROR: Model file not found at: {MODEL_PATH}")

    print(f"Directory contents: {os.listdir(os.path.dirname(MODEL_PATH))}")
    exit()

with open(MODEL_PATH, 'rb') as f:
    loaded_model = pickle.load(f)

def get_locations_from_dataset():
    try:
        df = pd.read_csv(DATASET_PATH)

        locations = df['Location'].unique().tolist()
        return sorted([loc for loc in locations if isinstance(loc, str)])
    except Exception as e:
        print(f"Error reading dataset: {e}")
        return location_names

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_locations', methods=['GET'])
def get_locations():
    return jsonify({'status': 'success', 'locations': get_locations_from_dataset()})

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