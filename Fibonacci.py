def fib(n):
    a=0
    b=1
    i=2
    if(n<0):
        print("You have entered the negative number")
        return
    if(n==0):
        return
    if(n==1):
        print(a)
        return
    print(a)
    print(b)
    while i<n:
        c=a+b
        a=b
        b=c
        i+=1
        print(c)

n=int(input("Enter the number of fibonacci series="))
fib(n)
