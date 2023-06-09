class BrandCode:
    def __init__(self):
        self.dataCodes = {
            "0": 'alfa romeo', "1": 'audi', "2": 'bmw', "3": 'chevrolet', "4": 'chrysler', "5": 'citroen',
            "6": 'dacia', "7": 'daewoo', "8": 'daihatsu', "9": 'fiat', "10": 'ford',
            "11": 'honda', "12": 'hyundai', "13": 'jaguar', "14": 'jeep', "15": 'kia',
            "16": 'lada', "17": 'lancia', "18": 'land rover', "19": 'mazda', "20": 'mercedes benz',
            "21": 'mini', "22": 'mitsubishi', "23": 'nissan', "24": 'opel', "25": 'peugeot',
            "26": 'porsche', "27": 'renault', "28": 'rover', "29": 'saad', "30": 'seat',
            "31": 'skoda', "32": 'smart', "33": 'subaru', "34": 'suzuki', "35": 'toyota',
            "36": 'trabant', "37": 'volkswagen', "38": 'volvo'
        }

    def translationCode(self, code: str) -> str:
        return self.dataCodes[code]
