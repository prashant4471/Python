# def greet():
#     print("Hello")
#     print("Good morning !!")
#
# greet()

# def add(x,y):
#     c=x+y
#     print(c)

# def add(x):
#     x=5
#     print(id(x))
#     return x
# a=2
# print(id(a))
# m=add(a)
# print(id(m))
#
# def add(lst):
#     print(id(lst))
#     lst[1]=25
#     print(lst)
#
# lst=[10,20,30]
# print(id(lst))
# add(lst)
# print(lst)


def fun(a,**b):
    print(a)
    for i,j in b.items():
        print(i,j)

fun('Prashant',age=20,city='BBSR',mob=8318)
