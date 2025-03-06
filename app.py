from flask import Flask, render_template,Request,jsonify
import pickle
import json
import numpy as np
import os
import pandas as pd

app = Flask(__name__)

# Load model and columns
try:
    with open( "./columns.json", "r") as f:
        data_columns = json.load(f)["data_columns"]
        locations = data_columns[3:]
except (FileNotFoundError, json.JSONDecodeError):
    data_columns, locations = [], []

try:
    with open( "./YTproject.pickle", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    model = None
@app.route('/')
def home():
    return "Hello, Flask is working!"


if __name__ == "__main__":
    app.run(debug=True)