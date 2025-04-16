from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = joblib.load('land_price_model.pkl')
encoder = joblib.load('location_encoder.pkl')

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