import os
import pickle
import pandas as pd
from flask import Flask, request, jsonify, render_template

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
        return sorted(['Ballygunge', 'Barrackpore', 'Santoshpur', 'Sarsuna',
       'Madhyamgram', 'Thakurpukur', 'Rajpur', 'North Dum Dum',
       'Dhakuria', 'Shyambazar', 'Nazirabad', 'Joka', 'Kasba', 'Barisha',
       'Behala', 'Taratala', 'Jodhpur Park', 'Salt Lake City', 'New Town',
       'Mohispota', 'Maheshtala', 'Naihati', 'Birati', 'Amtala',
       'Gariahat', 'New Barrakpur', 'Rajpur Sonarpur', 'Khardah',
       'Belghoria', 'Sodepur', 'Baghbazar', 'Baghajatin', 'Nimta',
       'Lake Gardens', 'Khidirpur', 'Kolutolla', 'Baguiati',
       'Diamond Harbour', 'Bantala', 'Tollygunge', 'Sinthi', 'Beliaghata',
       'Kamardanga', 'Netaji Nagar', 'Garia', 'Rajarhat', 'Kalikapur',
       'East Kolkata Township', 'Tangra', 'Bhowanipore', 'Bansdroni',
       'Kalighat', 'Ichapur', 'Mukundapur', 'Bramhapur', 'Hussainpur',
       'Berunanpukhuria', 'Kolkata', 'Bhatpara', 'Keshtopur',
       'Chinar Park', 'Baguihati', 'New Alipore', 'Kamdahari',
       'Paschim Putiary', 'Ganguly Bagan', 'Kaikhali', 'Garden Reach',
       'Picnic Garden', 'Haltu', 'Raghunathpur',
       'Baishnabghata Patuli Township', 'Srirampur', 'Agarpara',
       'Taltala', 'Entally', 'Purba Barisha', 'Dum Dum', 'Lake Town',
       'Ariadaha', 'Elgin', 'Purba Putiary', 'VIP Nagar', 'Barasat',
       'Jadavpur', 'Paschim Barisha', 'Alipore', 'Pailan', 'Garfa',
       'Shyamnagar', 'Ward No 113', 'Tagore Park', 'Sarada Pally',
       'Hanspukuria', 'Golf Green', 'Panchpota', 'Nayabad', 'Bijoygarh',
       'Kabardanga', 'Bow Bazaar', 'South Dum Dum', 'Dum Dum Cantonment',
       'Kamalgazi', 'Dakshin Gobindopur', 'Pancha Sayar', 'Beniapukur',
       'Kalagachhia', 'Chitpur', 'Rajabagan', 'Kalyan Nagar', 'Bangaon',
       'Champahati', 'Natagarh', 'Cossipore', 'Machuabazar', 'Habra',
       'Sewli Telinipara', 'Topsia', 'Kashipur', 'Shobhabazar',
       'Ashokgarh', 'Duttapukur', 'Bagnan', 'Park Street Area', 'Kalyani',
       'Budge Budge', 'Panihati', 'Narendrapur', 'Chowbaga', 'Saha Para',
       'Bamangachhi', 'Thakuranir Chak', 'Tala', 'Bamunpara', 'Paikpara',
       'Jorabagan', 'Krishnanagar', 'Maniktala', 'Regent Park',
       'Belgachia', 'Mominpore', 'Rahara', 'Bishnupur', 'Talbanda',
       'Bira', 'Barabazar Market', 'Bhatenda', 'Jorasanko', 'Khariberia',
       'Bagmari', 'Adarsha Nagar', 'Malickpur', 'Dunlop', 'Hedua',
       'Baranagar', 'Pansila', 'Garulia', 'Rania', 'College Square',
       'Chandpara', 'Kokapur', 'Bagpota', 'Dakshineswar', 'Beniatola',
       'Jugberia', 'Badartala', 'Hridaypur', 'Nabapally', 'Halisahar',
       'Airport', 'Tiljala', 'Natunhat', 'Palta', 'Baruipur', 'Fatepur',
       'Jagatipota', 'Naoabad', 'Sovabazar', 'Patipukur',
       'Aurobindo Park', 'Ramchandrapur', 'Gobra', 'Baruipur P',
       'Metiabruz', 'Vedic Village', 'Kanchrapara Loco', 'Basirhat',
       'Malancha Mahi Nagar', 'Kazipara', 'Kustia', 'Doperia Village',
       'Raja Bazar', 'Ruiya', 'Baithakkhana', 'Uttarbhag', 'Bow Barracks',
       'Abdalpur', 'Ultadanga', 'Maidan', 'Narayantala', 'Kankurgachi'])

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