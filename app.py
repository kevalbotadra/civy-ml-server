from flask import Flask
import flask
import predict


app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    budgetToPredict = flask.request.json["budgetList"]
    monthToPredict = flask.request.json["monthToPredict"]
    cateogry = flask.request.json["cateogry"]

    budget = predict.predictBudget(budgetToPredict=budgetToPredict, monthToPredict=monthToPredict, cateogry=cateogry)

    return {"budget" :  budget}

