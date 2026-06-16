from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    feature1 = float(request.form['feature1'])
    feature2 = float(request.form['feature2'])
    feature3 = float(request.form['feature3'])

    features = np.array([[feature1, feature2, feature3]])

    prediction = model.predict(features)

    if prediction[0] == 1:
        output = "Attack Detected"
    else:
        output = "Normal Traffic"

    return render_template('index.html',
                           prediction_text=output)

if __name__ == "__main__":
    app.run(debug=True)