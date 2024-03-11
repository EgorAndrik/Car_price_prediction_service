from flask import Flask, render_template, request
from json import load, dump

from model import CarRegressor
from carDetails import AddDetails
from translatBrandCode import BrandCode
from convertDataFrame import Сonverter


application = Flask(__name__, template_folder='template')


codesBrand = BrandCode()
model = CarRegressor()
addCar = AddDetails()
converter = Сonverter('DataFrames/TrainTestDATA.csv')


@application.route('/')
def HomePage():
    return render_template("index.html")


@application.route('/resultPrediction', methods=['POST'])
def resultPrediction():
    result = request.form
    resultDict = {i: result[i] for i in result}
    return render_template("resultPrediction.html", result=model.pred(resultDict))


@application.route('/resultPrediction/<userName>', methods=['POST'])
def resultPredictionUsers(userName: str):
    result = request.form
    resultDict = {i: result[i] for i in result}
    userPredData = [result[i] for i in result][:8]
    price = model.pred(resultDict)
    userPredData.append(price)
    userPredData[3] = codesBrand.translationCode(userPredData[3])
    with open('Logins/Logins.json', 'r') as logs:
        logins = load(logs)
    with open('Logins/Logins.json', 'w') as logs:
        logins[userName][1].append(userPredData)
        dump(logins, logs, ensure_ascii=False, indent='\t')
    return render_template("resultPrediction.html", result=price)


@application.route('/AddCarDetails', methods=['POST'])
def addCarDetails():
    result = request.form
    addCar.addData({i: result[i] for i in result})
    return render_template("AdminDirectory/AdminIndex.html")


@application.route('/LogIn', methods=['POST'])
def logIn():
    login = request.form
    try:
        with open('Logins/Logins.json', 'r') as logs:
            logIn_user = load(logs)[login['userName']]
        if login['userName'] == 'AdminData':
            return addCarFormAdmin() \
                if login['password'] == logIn_user \
                else 'ERROR access denied'
        else:
            return render_template(
                'UserIndex.html',
                userName=login['userName'],
                urlHistoryPred=f"/HistoriPred/{login['userName']}",
                urlPred=f"/resultPrediction/{login['userName']}"
            ) if login['password'] == logIn_user[0] else 'ERROR access denied'
    except KeyError:
        return 'ERROR This user is not registered'


@application.route('/Registration', methods=['POST'])
def registration():
    registrationForm = request.form
    with open('Logins/Logins.json', 'r') as logs:
        logins = load(logs)
    if registrationForm['userName'] not in logins:
        with open('Logins/Logins.json', 'w') as logs:
            logins[registrationForm['userName']] = [registrationForm['password'], []]
            dump(logins, logs, ensure_ascii=False, indent='\t')
        return render_template(
            'UserIndex.html',
            userName=registrationForm['userName'],
            urlHistoryPred=f"/HistoriPred/{registrationForm['userName']}",
            urlPred=f"/resultPrediction/{registrationForm['userName']}"
        )
    return "ERROR This user is registered on this service"


@application.route('/userPage/<userName>')
def userPage(userName: str):
    return render_template(
        'UserIndex.html',
        userName=userName,
        urlHistoryPred=f"/HistoriPred/{userName}",
        urlPred=f"/resultPrediction/{userName}"
    )


@application.route('/HistoriPred/<userName>')
def historyPredCars(userName: str):
    try:
        with open('Logins/Logins.json', 'r') as logs:
            dataPredUser = load(logs)[userName][1]
        return render_template(
            'historyPredCars.html',
            dataPredUser=dataPredUser,
            userName=userName,
            urlUserPage=f"/userPage/{userName}"
        )
    except KeyError:
        return 'KeyError'


@application.route('/AdminData/convertData')
def convertData():
    converter.convert()
    return "data convert"


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
