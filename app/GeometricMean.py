import numpy as np


class GeometricMean:
    @staticmethod
    def get(data):
        data_prod = 1
        exponent = 1 / len(data)
        for d in data:
            data_prod *= d ** exponent
        return data_prod
