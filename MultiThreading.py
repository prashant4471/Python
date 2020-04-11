from threading import *
from time import *
class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)                #giving a gap of 1 sec after execution of 1 loop iteration

t1=hello()
t2=hi()

t1.start()                #for creating a thread
sleep(0.2)                #for avoiding collision
t2.start()

t1.join()                #Bye will be printed when both the threads comes to main after execution from cpu
t2.join()
print("Bye")