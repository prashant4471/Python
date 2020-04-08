# def fac(n):
#     if(n==0):
#         print("1")
#     c=1
#     for i in range(1,n+1):
#         c=c*i
#     print("Factorial of this number=",c)
#
# n=int(input("Enter the number="))
# fac(n)

# Factorial through Recursion

def fac(n):
    if(n==0 or n==1):
        return 1;
    if(n>1):
        return n*fac(n-1)

n=int(input("Input the number="))
x=fac(n)
print(x)
