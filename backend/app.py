from flask import Flask, jsonify, request
import pickle
from flask_cors import CORS

# Load the model and encoders using pickle
with open("self_esteem_predictor.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("encoders.pkl", "rb") as encoders_file:
    encoder = pickle.load(encoders_file)  # Dictionary of encoders

print("Encoder keys:", encoder.keys())  # Check the available keys

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow testing from different origins

@app.route("/api/predict", methods=["POST"])
def predict():
    try:
        # Hardcoded data for testing
        # data=request.json
        # print(data)
        data = {
    "what's your age?": ["18 - 24"],  # Example input data
    "what's your height?": ["5'6'' - 5'10'' (167 - 178 cm)"],
    "what's your weight range?": ["61 - 70 kg"],
    "how often do you worry about your body image?": ["sometimes"],
    "how many hours do you spend on social media each day?": ["3 - 4 hours"],
    "how often do you compare your appearance to others on social media or in real life?": ["often"],
    "do you work out regularly?": ["yes"],
    "do you follow a specific diet?": ["yes, a vegetarian or vegan diet"],
    "do you feel that you need validation in your life?": ["yes, I feel the need for validation frequently"]
}
        
        # Extract features from the hardcoded data and encode them using the correct encoders
        features = [
            encoder["what's your age?"].transform([data["what's your age?"]])[0],
            encoder["what's your height?"].transform([["5'6'' - 5'10'' (167 - 178 cm)"]])[0],
            encoder["what's your weight range?"].transform([data["what's your weight range?"]])[0],
            encoder["how often do you worry about your body image?"].transform([data["how often do you worry about your body image?"]])[0],
            encoder["how many hours do you spend on social media each day?"].transform([data["how many hours do you spend on social media each day?"]])[0],
            encoder["how often do you compare your appearance to others on social media or in real life?"].transform([data["how often do you compare your appearance to others on social media or in real life?"]])[0],
            encoder["do you work out regularly?"].transform([data["do you work out regularly?"]])[0],
            encoder["do you follow a specific diet?"].transform([data["do you follow a specific diet?"]])[0],
            encoder["do you feel that you need validation in your life?"].transform([data["do you feel that you need validation in your life?"]])[0]
        ]

        # Predict self-esteem using the model
        prediction = model.predict([features])[0]

        # Debugging: Print prediction
        print("Prediction:", prediction)

        # Return the prediction as a JSON response
        return jsonify({"prediction": round(prediction, 4)})

    except Exception as e:
        print("Error occurred:", str(e))
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
