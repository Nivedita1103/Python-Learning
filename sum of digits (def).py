#adding the digits of given number
   
def getSum(n): #12345,1234,123,12,1,0
    sum = 0
    while (n != 0): #12345,1234,123,12,1,0 (loop is terminated)
        sum = sum+(n%10) #sum=5,sum=9,sum=12,sum=14,sum=15
        n = n // 10 #n=1234,123,12,1,0
    return sum
n = 123456767677 # or through user input prompt
print(getSum(n))
