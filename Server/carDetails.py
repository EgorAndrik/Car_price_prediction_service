import pandas as pd


class AddDetails:
    def __init__(self, data: dict):
        self.additionalData = data

    def addData(self):
        df = pd.read_csv('DataFrames/TrainTestDATA.csv').iloc[:, 1:]
        insertData = [int(self.additionalData['price']), self.additionalData['vehicleType'],
                      int(self.additionalData['yearOfRegistration']), self.additionalData['gearbox'],
                      int(self.additionalData['powerPS']), int(self.additionalData['kilometer']),
                      self.additionalData['fuelType'],
                      self.additionalData['brand'].lower() if len(self.additionalData['brand'].split()) == 1
                      else '_'.join(map(lambda x: x.lower(), self.additionalData['brand'].split())),
                      int(self.additionalData['notRepairedDamage'])]

        df.loc[len(df.index)] = insertData
        df.to_csv('DataFrames/TrainTestDATA.csv')
        return 'Данные введены'
