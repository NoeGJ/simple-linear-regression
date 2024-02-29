import math

from DiscreteMaths import DiscreteMaths as dm

class SLR( dm ):
    def __init__( self, array1, array2 ):
        super().__init__( array1, array2 )
        self.bt1 = self.__toComputeBeta1()
        self.bt0 = self.__toComputeBeta0()
        self.r = self.__toComputeR()
        self.rSquared = self.__toComputeRSquared()

    def __toComputeBeta0(self):
        return (sum(self.y) - self.bt1 * sum(self.x)) / self.size()

    def __toComputeBeta1(self):
        return ((self.size() * (self.sumXY(self.x, self.y))) - ( self.sumXsumY(self.x, self.y) )) / ((self.size() * (self.sumXY(self.x, self.x))) - self.sumXquad( self.x ))

    def __toComputeR(self):
        num = ((self.size() * self.sumXY(self.x, self.y)) - (self.sumXsumY(self.x, self.y)))
        dem = math.sqrt((self.size() * self.sumXY(self.x, self.x) - (self.sumXsumY(self.x, self.x))) * (self.size() * self.sumXY(self.y, self.y) - (self.sumXsumY(self.y, self.y))))
        return num / dem

    def __toComputeRSquared(self):
        ssr = sum((yi - (self.toPredict(xi))) ** 2 for xi, yi in zip(self.x, self.y))
        tss = sum((yi - self.mean(self.y)) ** 2 for yi in self.y)
        return 1 - (ssr / tss)

    def getBeta0(self):
        return self.bt0

    def getBeta1(self):
        return self.bt1

    def toPredict(self, value):
        return self.bt0 + self.bt1 * value

    def getR(self):
        return self.r

    def getRSquared(self):
        return self.rSquared

    def toPrintRegEq(self, value):
        print( "{} + {} * {} = {}".format(self.bt0, self.bt1, value, self.toPredict(value)) )
