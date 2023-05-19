from flask import Flask, render_template, request
from model import CarRegressor
import pandas as pd

application = Flask(__name__, template_folder='template')


@application.route('/aboutModels')
def aboutModels():
    data = pd.read_csv('DataFrames/TrainTestDATA.csv')
    dictModelsCar = {i: list(data[data['brand'] == i]['model'].unique()) for i in data['brand'].unique()}
    return render_template("modelsCar.html", result=dictModelsCar)


@application.route('/resultPrediction', methods=['POST', 'GET'])
def resultPrediction():
    if request.method == 'POST':
        result = request.form
        resultDict = {i: result[i] for i in result}
        CR = CarRegressor()
        predict = CR.pred(resultDict)
        return render_template("resultPrediction.html", result=predict)


if __name__ == '__main__':
    application.run(debug=True)
