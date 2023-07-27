import pandas as pd


class Сonverter:
    def __init__(self, pathData: str):
        self.normalData = pd.read_csv(pathData).iloc[:, 1:]
        self.mainData = pd.read_csv('DataFrames/TrainTestDATA_Second.csv').iloc[:, 1:]

    def convert(self):
        self.normalData = pd.get_dummies(self.normalData, columns=['vehicleType'])
        self.normalData = pd.get_dummies(self.normalData, columns=['gearbox'])
        self.normalData = pd.get_dummies(self.normalData, columns=['fuelType'])

        self.normalData['brand'] = self.normalData['brand'].astype('category')
        self.normalData['brand'] = self.normalData['brand'].cat.codes

        self.normalData['notRepairedDamage'] = self.normalData['notRepairedDamage'].astype('category')
        self.normalData['notRepairedDamage'] = self.normalData['notRepairedDamage'].cat.codes

        for elem in self.normalData.iloc[:, :]:
            self.normalData[elem] = self.normalData[elem].map(int)

        resDataFrame = pd.concat([self.mainData, self.normalData])
        resDataFrame.to_csv('DataFrames/TrainTestDATA_Second.csv')