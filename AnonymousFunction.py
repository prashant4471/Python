# f=lambda a,b:a*b
#
# result=f(5,6)
# print(result)

# Use of filter(),map(),reduce()
# def is_even(a):
#     return a%2==0
from functools import reduce

nums=[3,7,2,1,5,8,6,9]

even=list(filter(lambda n : n%2==0,nums))

double=list(map(lambda n:n*2,even))

sum=reduce(lambda a,b:a+b,double)

print(even)
print(double)
print(sum)

