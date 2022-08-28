num = 25 #sum from 1 to 100 (num)
sum = 0
    
if num < 0:
    print("Enter a positive number")
else:
    # use while loop to iterate until zero
    while(num > 0): # 10,9,8,7...1, 0 ( loop will be terminated)
        sum += num #sum=sum+num, sum=10,sum=19,......sum=55
        num -= 1  #num=num-1, 9,8,7,...num=0
    print("The sum is", sum)
