from flask import Flask, jsonify, request
import pickle
import os

app = Flask(__name__)

# Load model
model_path = os.path.join(os.path.dirname(__file__), "../models/model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return jsonify({"message": "Flask app running on Google Cloud Run!"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if "input" not in data:
        return jsonify({"error": "Input data missing"}), 400

    # Example: model expects a number
    x = data["input"]
    y = model.predict([[x]])  # adjust based on your model

    return jsonify({"prediction": y[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
 