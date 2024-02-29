import math

from Dataset import DataSet

class DiscreteMaths(DataSet):
    def __init__(self, array1, array2):
        super().__init__(array1, array2)

    def sumXY(self, array1, array2):
        return sum((a * b for a, b in zip(array1, array2)))

    def sumXsumY(self, array1, array2):
        return sum(array1) * sum(array2)

    def sumXquad(self, array):
        return math.pow(sum(array), 2)

    def mean(self, array):
        return sum(array) / len(array)

