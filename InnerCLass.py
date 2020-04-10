class student:                            # Outer Class

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.laptop()

    def show(self):
        print(self.name)
        print(self.roll)
        self.lap.show()

    class laptop:                       # Inner Class

        def __init__(self):
            self.brand="HP"
            self.cpu=16
            self.ram=8

        def show(self):
            print((self.brand))
            print((self.cpu))
            print((self.ram))

s1=student("Prashant",1805)
s2=student("Jenni",1806)

s1.show()

