from flask import Flask, render_template, request
import json
from model import CarRegressor
from carDetails import AddDetails


application = Flask(__name__, template_folder='template')


@application.route('/')
def HomePage():
    return render_template("index.html")


@application.route('/resultPrediction', methods=['POST'])
def resultPrediction():
    result = request.form
    resultDict = {i: result[i] for i in result}
    predict = CarRegressor().pred(resultDict)
    return render_template("resultPrediction.html", result=predict)


@application.route('/AddCarDetails', methods=['POST'])
def addCarDetails():
    if request.method == 'POST':
        result = request.form
        AD = AddDetails({i: result[i] for i in result})
        AD.addData()
        return render_template("AdminDirectory/AdminIndex.html")


@application.route('/LogIn', methods=['POST'])
def logIn():
    login = request.form
    with open('Logins/Logins.json', 'r') as logs:
        logins = json.load(logs)
        if login['userName'] in logins:
            if login['userName'] == 'AdminData':
                return render_template(logins['AdminData'][1], result='ok') \
                    if login['password'] == logins['AdminData'][0] \
                    else 'ERROR access denied'
            else:
                return render_template('UserIndex.html', userName=login['userName']) \
                    if login['password'] == logins[login['userName']] \
                    else 'ERROR access denied'
        return 'ERROR access denied'


@application.route('/Registration', methods=['POST'])
def registration():
    registrationForm = request.form
    with open('Logins/Logins.json', 'r') as logs:
        logins = json.load(logs)
    if registrationForm['userName'] not in logins:
        with open('Logins/Logins.json', 'w') as logs:
            logins[registrationForm['userName']] = registrationForm['password']
            json.dump(logins, logs, ensure_ascii=False, indent='\t')
        return render_template('UserIndex.html', userName=registrationForm['userName'])
    return "ERROR This user is registered on this service"


@application.route('/AdminData/PredictonPriceAdmin')
def predictonPriceAdmin():
    return render_template('AdminDirectory/PredictionAdmin.html')


@application.route('/AdminData/AddCarFormAdmin')
def addCarFormAdmin():
    return render_template('AdminDirectory/AdminIndex.html')


@application.route('/LoginIndex')
def loginIndex():
    return render_template('LoginIndex.html')


@application.route('/RegistrationIndex')
def registrationIndex():
    return render_template('RegistrationIndex.html')


if __name__ == '__main__':
    application.run(debug=True)
