import numpy as np
import pandas as pd
import pickle


class CarRegressor:
    def __init__(self):
        self._modelRegressor = pickle.load(open('models/bestModelFourth.bf', 'rb'))

    def _convertData(self, data: dict) -> np.ndarray:
        dt = pd.read_csv('DataFrames/TrainTestDATA_Second.csv').iloc[:1, 2:]
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
        for elem in [vechicleType, gearbox, fuelType]:
            for el in elem:
                dt[el] = elem[el]
        dt = np.array(dt)
        return dt

    def pred(self, X: dict) -> float:
        dataPred = self._convertData(X)
        prediction = self._modelRegressor.predict(dataPred)
        return round(prediction[0] * 2, 3)
