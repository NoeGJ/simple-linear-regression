#import customtkinter
import tkinter

import math

class linear_regression:
    def __init__(self):

        self.y = [651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518]
        self.x = [23, 26, 30, 34, 43, 48, 52, 57, 58]
        self.n = len(self.x)

        self.b1 = ((self.n * (self.sumMul(self.x, self.y))) - (sum(self.x) * sum(self.y))) / ((self.n * (self.sumMul(self.x, self.x))) - math.pow(sum(self.x), 2))
        self.b0 = (sum(self.y) - self.b1 * sum(self.x)) / self.n

        ssr = sum((yi - (self.b0 + self.b1 * xi)) ** 2 for xi, yi in zip(self.x, self.y))

        y_mean = sum(self.y) / self.n
        tss = sum((yi - y_mean) ** 2 for yi in self.y)
        self.r_squared = 1 - (ssr / tss)

    def sumMul(self,x, y):
        return sum((a * b for a, b in zip(x, y)))

    def getBeta1(self):
        return self.b1

    def getBeta0(self):
        return self.b0

    def getR_squared(self):
        return self.r_squared

    def getPrediction(self, value):
        return round(self.b0) + round(self.b1) * value

xpredict = [15, 20, 25, 60, 63]

lr = linear_regression()

print("beta1 =", lr.getBeta1())
print("beta0 =", lr.getBeta0())
for i in xpredict:
    print(round(lr.getBeta0()), '+', round(lr.getBeta1()),'*', + i)
    print('Prediccion de', i, str(lr.getPrediction(i)))

print("R^2 =", lr.getR_squared())
print("R =", math.sqrt(lr.getR_squared()))

