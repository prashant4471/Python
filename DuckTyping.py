# when the object has the method execute , if it can be of any class ,it will work
# Duck Typing means whe object should have same behaviour which means same method or function.
class Pycharm:

    def execute(self):
        print("Compiling")
        print("Executing")


class Myeditor:
    def execute(self):
        print("Spell Check")
        print("Convention check")
        print("Compiling")
        print("Executing")

class laptop:

    def code(self,ide):
        ide.execute()

# ide=Pycharm()
ide=Myeditor()

lap1=laptop()
lap1.code(ide)