a=["a","b",1,2,3,4,3,2,1]
a=str(a) #coverted string list a
n=input("Enter the element")
c=a.count(n)
if(c==0):
    print("not in list")
else:
    print("the elemnt",n," occurs",c," times")
