import numpy as np
import pandas as pd


class AddDetails:
    def __init__(self, data: dict):
        self.additionalData = data

    def addData(self):
        df = pd.read_csv('DataFrames/TrainTestDATA_Second.csv').iloc[:, 1:]
        insertData = [int(self.additionalData['price']), int(self.additionalData['yearOfRegistration']),
                      int(self.additionalData['powerPS']), int(self.additionalData['kilometer']),
                      int(self.additionalData['brand']), int(self.additionalData['notRepairedDamage'])]
        vechicleType = {i: int(i == self.additionalData['vehicleType']) for i in
                        ['vehicleType_bus', 'vehicleType_cabrio', 'vehicleType_coupe',
                         'vehicleType_limousine', 'vehicleType_others', 'vehicleType_small car',
                         'vehicleType_station wagon', 'vehicleType_suv']}
        gearbox = {i: int(i == self.additionalData['gearbox']) for i in ['gearbox_automatic', 'gearbox_manual']}
        fuelType = {i: int(i == self.additionalData['fuelType']) for i in ['fuelType_cng', 'fuelType_diesel', 'fuelType_electro',
                                                            'fuelType_hybrid', 'fuelType_lpg', 'fuelType_petrol']}
        for i in vechicleType:
            insertData.append(vechicleType[i])
        for i in gearbox:
            insertData.append(gearbox[i])
        for i in fuelType:
            insertData.append(fuelType[i])

        df.loc[len(df.index)] = insertData
        df.to_csv('DataFrames/TrainTestDATA_Second.csv')
        return 'Данные введены'