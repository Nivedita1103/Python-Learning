n = 45062
rev = 0
    
while (n > 0): #n=4562, 456, 45,4,0 (terminated)
    a = n % 10 #a=2, a=6, a=5,a=4
    rev = rev * 10 + a # rev=0*10+2=2, rev=2*10+6=26,rev=26*10+5=265, rev=265*10+4=2654
    n = n // 10 #n=456,45,4,0
    
print(rev)
