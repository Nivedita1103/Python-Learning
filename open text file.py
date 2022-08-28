myfile=open(r'E:\previous work\cs file\poem.txt',"r")
str=" "
while str:
    str=myfile.readline()
    print(str,end='')
myfile.close()
