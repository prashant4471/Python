a=10

# def fun():
#     global a
#     a=15
#     print(a)
print(id(a))
def fun():
    a=9
    x=globals()['a']
    print(id(x))
    globals()['a']=15
    print(a)

fun()

print(a)
print(id(a))