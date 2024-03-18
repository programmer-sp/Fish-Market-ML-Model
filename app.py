import os
import numpy as np
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("fish_market_model.pkl", "rb"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Get user input
    length1 = float(request.form["length1"])
    length2 = float(request.form["length2"])
    length3 = float(request.form["length3"])
    height = float(request.form["height"])
    width = float(request.form["width"])

    # Make prediction
    features = np.array([[length1, length2, length3, height, width]])
    prediction = model.predict(features)

    return render_template("index.html", prediction=prediction[0])


if __name__ == "__main__":
    # Use the PORT environment variable provided by Heroku
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host="0.0.0.0", port=port)
    app.run(debug=True)
