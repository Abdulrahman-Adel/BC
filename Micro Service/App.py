# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 15:05:02 2020

@author: Abdelrahman
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("finalized_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    """
    For rendering results on HTML GUI
    """
    features = [np.array([x for x in request.form.values()])]
    prediction = model.predict(features)


    return render_template("index.html", prediction_text="Class Label should be $ {}".format(prediction))


if __name__ == "__main__":
    app.run(debug=False)

