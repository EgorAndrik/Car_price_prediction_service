from flask import Flask, render_template, request
from model import CarRegressor


application = Flask(__name__, template_folder='template')


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
