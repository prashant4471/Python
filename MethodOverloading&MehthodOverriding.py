#In Python, we don't have the by default concept of Method Overloading but we achieve it by defining it by if-else block
#
# class student:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#
#     def sum(self,a=None,b=None,c=None):
#         s=0
#         if a!=None and b!=None and c!=None:
#             s=a+b+c
#         elif a!=None and b!=None:
#             s=a+b
#         else:
#             s=a
#         return s
#
# s1=student(2,3)
#
# print(s1.sum(3))


#Method Overriding

class A:
    def show(self):
        print("In A show")

class B(A):
    # pass
    def show(self):
        print("IN B show")


a1=A()
b1=B()

a1.show()
b1.show()