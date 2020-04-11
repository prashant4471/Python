# f=open('Mydata.txt',"r")        #reading from a file
# # print(f.read())
# print(f.readline(),end="#")
# print(f.readline())

# f2=open('Mydata.txt',"a")         #appending in file
# f2.write("Writing in the file")

# f3=open("abc","w")                  #writing in the file
# f3.write("Writing in the file abc")

f4=open('Mydata.txt',"r")

f5=open('abc',"w")

for data in f4:
    f5.write(data)                # copying data in file abc from file Mydata