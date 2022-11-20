import pickle
from flask import Flask, jsonify, request

from flask_cors import CORS
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

CORS(app)

with open("./rf-model.pkl", "rb") as file:
    model: RandomForestClassifier = pickle.load(file)

with open("./orders_with_features.pkl", "rb") as file:
    orders: pd.DataFrame = pd.read_pickle(file)

@app.post("/predict")
def predict():
    body = request.get_json()

    company_id = body.get("company_id")

    user_orders = orders[orders.company_id == company_id]

    user_orders = user_orders.drop(['reordered'], axis=1)

    predictions = model.predict(user_orders)

    products = user_orders[predictions == 1]

    print(products[:5])

    return jsonify(success=True)
