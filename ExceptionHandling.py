a=5
b=0

try:
    print("Resource Opened")
    print(a/b)
    k=int(input("Enter a number="))
    print(k)
except ZeroDivisionError as e:                             # Error block for Zero Dvision Error
    print("Hey, you can't divide a number by zero ",e)
except ValueError as f:                                    # Error block for Value Error
    print("You have not entered an number ",e)
except Exception as g:                                     # Error if any other error occurs
    print("Unknown Error")
finally:                                                   # This block will execute no matter what happens in try-except block
    print("Resource Closed")
