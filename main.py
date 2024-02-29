from  Simple_linear_regression import SLR

class Main:
    def __init__(self):
        self.y = [651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518]
        self.x = [23, 26, 30, 34, 43, 48, 52, 57, 58]
        self.xpredict = [15, 20, 25, 60, 63]
        self.lr = SLR(self.x, self.y)

    def printSLR(self):
        print("Beta 0 =", self.lr.getBeta0())
        print("Beta 1 =", self.lr.getBeta1())
        for i in self.xpredict:
            self.lr.toPrintRegEq(i)
        print("R^2 =", self.lr.getRSquared())
        print("R =", self.lr.getR())

main = Main()
main.printSLR()


