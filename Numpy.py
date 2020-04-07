from numpy import *

# arr=arange(1,15,4)
# arr=linspace(0,2)
# arr=logspace(1,40,5)
# arr=zeros(5,int)
# arr=ones(5)

arr1=array([1,2,3,4,5])
arr2=array([2,5,3,7,9])

# arr=arr+5


# arr3=arr1+arr2

# print(unique([arr1,arr2]))

# coping an array
# 1.Shallow Copying
# arr3=arr1.view()
# arr1[1]=9
# print(arr1)
# print(arr3)

# 2.Deep Copying
arr3=arr1.copy()
arr1[1]=9
print(arr1)
print(arr3)
