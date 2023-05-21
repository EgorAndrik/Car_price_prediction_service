import numpy as np
import pandas as pd
import pickle
from catboost import CatBoostRegressor


class CarRegressor:
    def __init__(self):
        self.modelRegressor = pickle.load(open('models/bestModelFourth.bf', 'rb'))

    def _convertData(self, data: dict) -> np.ndarray:
        dt = pd.read_csv('DataFrames/TrainTestDATA_Second.csv').iloc[:1, 2:]

        dt = pd.get_dummies(dt, columns=['vehicleType'])
        dt = pd.get_dummies(dt, columns=['gearbox'])
        dt = pd.get_dummies(dt, columns=['fuelType'])
        dt['brand'] = dt['brand'].astype('category')
        dt['brand'] = dt['brand'].cat.codes
        dt['notRepairedDamage'] = dt['notRepairedDamage'].astype('category')
        dt['notRepairedDamage'] = dt['notRepairedDamage'].cat.codes
        for elem in dt.iloc[:, :]:
            dt[elem] = dt[elem].map(int)

        vechicleType = {i: int(i == data['vehicleType']) for i in
                        ['vehicleType_bus', 'vehicleType_cabrio', 'vehicleType_coupe',
                         'vehicleType_limousine', 'vehicleType_others', 'vehicleType_small car',
                         'vehicleType_station wagon', 'vehicleType_suv']}
        gearbox = {i: int(i == data['gearbox']) for i in ['gearbox_automatic', 'gearbox_manual']}
        fuelType = {i: int(i == data['fuelType']) for i in ['fuelType_cng', 'fuelType_diesel', 'fuelType_electro',
                                     'fuelType_hybrid', 'fuelType_lpg', 'fuelType_petrol']}

        dt['yearOfRegistration'] = int(data['yearOfRegistration'])
        dt['powerPS'] = int(data['powerPS'])
        dt['kilometer'] = int(data['kilometer'])
        dt['brand'] = int(data['brand'])
        dt['notRepairedDamage'] = int(data['notRepairedDamage'])

        for i in vechicleType:
            dt[i] = vechicleType[i]
        for i in gearbox:
            dt[i] = gearbox[i]
        for i in fuelType:
            dt[i] = fuelType[i]

        dt = np.array(dt)
        return dt

    def pred(self, X: dict):
        dataPred = self._convertData(X)
        prediction = self.modelRegressor.predict(dataPred)
        return round(prediction[0] * 2.5, 3)
