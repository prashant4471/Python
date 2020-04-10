class computer:

    def __init__(self):
        self.name="Prashant"
        self.age=20

    def update(self):
        self.age=18

    def compare(self,c2):
        if self.age==c2.age:
            return True
        else:
            return False



c1=computer()
c2=computer()

c1.update()

if c1.compare(c2):
    print("Same")
else:
    print("Not Same")



print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)


# print(id(c1))
# print(id(c2))