class a:

    def __init__(self):
        print("In A init")

    def feature1(self):
        print("Feature 1 in a working ...")

    def feature2(self):
        print("Feature 2 working ...")

class b:                               # Single Level Inheritance

    def __init__(self):
        # super().__init__()
        print("In B Init")

    def feature1(self):
        print("Feature 1 in b working ...")

    def feature4(self):
        print("Feature 4 working ...")

class c(a,b):

    def __init__(self):
        super().__init__()
        print("In C Init")

    def fea(self):
        super().feature2()


c1=c()
c1.feature1()
c1.fea()