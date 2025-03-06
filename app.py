from flask import Flask, render_template
import json
import pickle
app = Flask(__name__)


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
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
