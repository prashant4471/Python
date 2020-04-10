class Computer:

    def __init__(self,cpu,ram):
       self.cpu=cpu
       self.ram=ram

    def conf(self):
        print("Config is ",self.cpu,self.ram)



com1=Computer('i5',16)
com2=Computer('Prison 3',8)

Computer.conf(com1)
Computer.conf(com2)

# com1.conf()
# com2.conf()