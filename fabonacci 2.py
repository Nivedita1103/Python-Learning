def fibonacci(n):
    i=0
    a=0
    b=1
    if n<=0:
        print("incorrect input")
    elif n==1:
        return b
    else:
        for i in range(0,n):
            c=a+b
            a=b
            b=c
            print(b)
            i=i+1
        return " "
n=int(input("enter last term"))
print (fibonacci(n))
