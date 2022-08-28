def fibonacci(n):
    a = 0 #first=0
    b = 1 #second=1
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return b
    else:
        for i in range(0, n): #0,1,2,3,4
            c = a + b #next=first+second # 1 2 3 5,,8,13(first), 21(second), 34(next)
            a = b     #f=s      # now (second,8) as first (one location prior, ls)
            b = c     #s=next   # now next (13) becomes second (becomes second)
            print(b)
        return b
   
   
# Driver Program
print(fibonacci(5))
