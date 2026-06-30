# Predicting Property Valuations for Kolkata

Machine learning-powered real estate price estimation across Kolkata's neighborhoods.<br>
**Link:** [https://house-price-predictor-kolkata-1.onrender.com/]
---

## About the Project

This project builds an end-to-end property valuation tool for the Kolkata real estate market. Given a flat's built-up area, number of rooms (BHK), and neighborhood, the model predicts its market price in Crores (₹ Cr).

The machine learning pipeline is trained on 3,500+ real Kolkata property listings and uses an Extra Trees Regression model wrapped in a scikit-learn Pipeline, ensuring consistent preprocessing at both training and inference time. The model is served through a lightweight Flask web application with a clean, responsive frontend.

---

## Features

- Predicts flat prices across 200+ Kolkata neighborhoods
- Extra Trees Regressor achieving R² of 0.95 on the test set
- Automated outlier removal based on price-per-sqft and room-size sanity checks
- Flask REST API with a `/predict` endpoint accepting JSON input
- Responsive glassmorphism UI with dynamic location dropdown

---

## Project Structure

```
Read directory.txt
```

---

## Dataset

**Name:** House_Price.csv  
**Source:** [https://www.kaggle.com/datasets/kuntalmaity/house-price](https://www.kaggle.com/datasets/kuntalmaity/house-price)

Download the dataset from Kaggle and place it at `dataset/raw/House_Price.csv` before running the notebook.

The dataset contains ~3,968 property listings across Kolkata with the following columns:

| Column | Description |
|---|---|
| `Flat_Price` | Listing price (e.g. "₹8.5 Cr", "₹45 L") |
| `BHK` | Room configuration (e.g. "3 BHK") |
| `Location` | Neighborhood name within Kolkata |
| `Total_Sq.ft` | Built-up area (e.g. "1450 sq.ft") |

---

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/your-username/Kolkata_House_Price_Predictor.git
cd Kolkata_House_Price_Predictor
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Download the dataset**

Download `House_Price.csv` from the Kaggle link above and place it at `dataset/raw/House_Price.csv`.

**4. Run the notebook**

Open `notebooks/cleaning_data.ipynb` and run all cells. This cleans the data, trains the model, and saves `final_production_model.pkl` to `ml_core/`.

**5. Start the Flask server**
```bash
cd web_app
python main.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

## Tech Stack

| Layer | Technology |
|---|---|
| ML Model | scikit-learn (ExtraTreesRegressor) |
| Data Processing | pandas, numpy |
| Web Server | Flask |
| Frontend | HTML, CSS, Vanilla JS |
| Notebook | Jupyter |

---

## License

This project is for educational purposes.  
Dataset credits: [Kuntal Maity](https://www.kaggle.com/datasets/kuntalmaity/house-price) on Kaggle.