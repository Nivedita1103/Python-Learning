a=["a","b",1,2,3,4,3,2,1] #list with multiple data types
n=input("Enter the element to be searched") #string 1
count=0
for i in a: #loop on the elements of list a
    if(n==str(i)): # n=1; 1==(a,b,1,2,3,4,...1) #if(n==i)?
            count=count+1
if(count==0):
    print("not in list")
else:
    print("the element",n," occurs", count," times")
   
#for tuples, strings and dict
