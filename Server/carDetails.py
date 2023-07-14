import pandas as pd


class AddDetails:
    def __init__(self):
        self.mainData = pd.read_csv('DataFrames/TrainTestDATA.csv').iloc[:, 1:]

    def addData(self, data: dict):
        insertData = [
            int(data['price']), data['vehicleType'],
            int(data['yearOfRegistration']), data['gearbox'],
            int(data['powerPS']), int(data['kilometer']),
            data['fuelType'],
            data['brand'].lower() if len(data['brand'].split()) == 1
            else '_'.join(map(lambda x: x.lower(), data['brand'].split())),
            'yes' if int(data['notRepairedDamage']) else 'no'
        ]

        self.mainData.loc[len(self.mainData.index)] = insertData
        self.mainData.to_csv('DataFrames/TrainTestDATA.csv')
