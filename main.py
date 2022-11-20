from flask import request
from app import app

@app.route("/predict")
def predict():
    body = request.data

    company_category_id = body.company_category_id

    print(company_category_id)
