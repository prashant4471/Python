class student:

    school="KIIT"

    def __init__(self,m1,m2,m3):               #Constructor
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):                           #Accessor Method(Instance Method)
        return (self.m1+self.m2+self.m3)/3

    def get(self):                           #Mutator Method(Instance Method)
        print(self.m1)

    @classmethod
    def getschool(cls):                           #Class Method(works with class variable)
        return cls.school

    def info():
        print("This is student class....")

s1=student(14,17,18)
s2=student(18,19,16)

s1.get()
print(s1.avg())
print(student.getschool())
student.info()
