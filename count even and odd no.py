n=int(input("Enter limit")) #10
   
odd=0
even=0
#if (true) print odd
for i in range(1,n+1,2): # 13579
    print(i)
    odd=odd+1 #adding odd nums
print("odd:",odd)
   
#else (print even)
for i in range(2,n+1,2):#246810
    print(i)
    even=even+1 #adding even nums
print("even:",even)
