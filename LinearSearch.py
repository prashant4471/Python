pos=-1

def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False

list=[5,3,7,8,9]
n=9

if search(list,n):
    print("Found at index ",pos)
else:
    print("Not Found")