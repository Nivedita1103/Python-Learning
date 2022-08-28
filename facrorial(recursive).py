#Recursive function

def factorial(n): #5,4,3,2,1
    if n == 0: #5,4...0
        return 1
    else:
        return n * factorial(n-1) # 5*4*3*2*1
n=int(input("Enter a number : ")) #5
print(factorial(n))
   
   
#for and range or any others to do factorial computation ?
