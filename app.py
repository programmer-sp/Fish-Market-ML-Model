from flask import Flask, render_template, request
# import pickle
# import numpy as np

app = Flask(__name__)

# Load the trained model
# with open('fish_market_model.pkl', 'rb') as model_file:
#     model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get user input
#     length1 = float(request.form['length1'])
#     length2 = float(request.form['length2'])
#     length3 = float(request.form['length3'])
#     height = float(request.form['height'])
#     width = float(request.form['width'])

#     # Make prediction
#     features = np.array([[length1, length2, length3, height, width]])
#     prediction = model.predict(features)

#     return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)