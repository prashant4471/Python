# import array as arr
#
# val=arr.array('i',[1,2,3,4,5])
# # val.reverse()
# print(len(var))





from array import *
arr=array('i',[])

n=int(input("Enter the length of the array="))

for i in range(n):
    x=int(input("Enter the next value="))
    arr.append(x)

m=int(input("Enter the value to get the index number="))
# n=0
# for i in arr:
#     n=n+1
#     if i==m:
#         print(n-1)
#         break
# else:
#     print("number not found")

print(arr.index(m))