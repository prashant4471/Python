from abc import ABC,abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass

# class whiteboard(computer):
#     def write(self):
#         print("It's writing")


class Laptop(computer):
    def process(self):
        print("It's running")


class Programmer:
    def work(self,com):
        print("Solving Bugs")
        com.process()

# com=computer()                 object can't be created bcz computer is an abstract class

com1=Laptop()
com1.process()

# com2=whiteboard()

prog=Programmer()
prog.work(com1)

# prog.work(com2)