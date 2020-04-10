class a:

    def feature1(self):
        print("Feature 1 working ...")

    def feature2(self):
        print("Feature 2 working ...")

class b(a):                               # Single Level Inheritance

    def feature3(self):
        print("Feature 3 working ...")

    def feature4(self):
        print("Feature 4 working ...")

a1=a()
a1.feature1()
a1.feature2()

b1=b()
b1.feature3()
b1.feature4()
b1.feature2()
b1.feature1()