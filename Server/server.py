from flask import Flask, render_template, request
from model import CarRegressor
from carDetails import AddDetails


application = Flask(__name__, template_folder='template')


@application.route('/resultPrediction', methods=['POST', 'GET'])
def resultPrediction():
    if request.method == 'POST':
        result = request.form
        resultDict = {i: result[i] for i in result}
        CR = CarRegressor()
        predict = CR.pred(resultDict)
        return render_template("resultPrediction.html", result=predict)


@application.route('/AddCarDetails', methods=['POST'])
def addCarDetails():
    if request.method == 'POST':
        result = request.form
        AD = AddDetails({i: result[i] for i in result})
        return render_template("adminRes.html", result=AD.addData())


if __name__ == '__main__':
    application.run(debug=True)
