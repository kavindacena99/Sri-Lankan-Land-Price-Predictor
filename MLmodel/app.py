from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
CORS(app)

land_price_model = os.path.join(BASE_DIR, 'land_price_model.pkl')
location_encoder = os.path.join(BASE_DIR, 'location_encoder.pkl')

model = joblib.load(land_price_model)
encoder = joblib.load(location_encoder)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    location = data["location"]
    size = float(data["size"])
    #print(f"Received data: {data}")

    try:
        encoded_location = encoder.transform([location])[0]
        prediction = model.predict([[encoded_location, size]])[0]
        return jsonify({"predicted_price": round(prediction,2)})
    
    except:
        return jsonify({"error": "Invalid location or size"}), 400
    
if __name__ == '__main__':
    app.run(debug=True)