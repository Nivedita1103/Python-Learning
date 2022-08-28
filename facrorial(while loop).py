fact = 1
n=int(input("Enter the value")) #6
if n<0: #n=6
    print("Enter other numbers")
elif n==0: #0!=1 #6
    print(1)
else:
    while (n >= 1):#6,5, 4,3,2,1,0 (terminate)
        fact *= n #fact=fact*n # fact=6, fact=6*5,, fact=30*4, fact=120*3, fact=360*2, fact=720*1=720
        n=n-1  #n=6-1,n=5-1,n=4-1,n=3-1,n=2-1,n=1-1, n=0
print(fact)
