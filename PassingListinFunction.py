

# def count(lst):
#     odd=0
#     even=0
#     for i in lst:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#     print("Even=",even)
#
#     print("Odd=",odd)
#
#
# lst=[1,2,3,4,5,6,7,8]
#
# count(lst)


# Counting the no of characters in each word and printing those words whose length is greater than 5

list=("Ramu","Prashant","Ramesh","Siera")

def count(lst):
    for i in lst:
        x=len(i)
        if x>5:
            print(i)

count(list)


