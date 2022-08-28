b1=input("enter hex number") #string only for Base 2,8,16 inputs,1010
a=int(b1,2) # hex input (var,input base number), a is decimal value
   
b=oct(a)
c=bin(a)
    
print(a) #decimal
print(b) #octal
print(c) #binary
