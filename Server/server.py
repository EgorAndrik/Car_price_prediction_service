from flask import Flask, render_template, request
import json
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


@application.route('/LogInAdmin', methods=['POST'])
def logInAdmin():
    login = request.form
    with open('Logins/Logins.json', 'r') as logs:
        logins = json.load(logs)
        if login['userName'] in logins:
            return render_template("AdminIndex.html", result='ok') if login['password'] == logins['AdminData']\
                else 'ERROR access denied'
        return 'ERROR access denied'


if __name__ == '__main__':
    application.run(debug=True)
