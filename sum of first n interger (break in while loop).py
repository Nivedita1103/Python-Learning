num_sum = 0
count = 0
while(count<10): #[0,1,2,3,4,5,,,,9]
    num_sum = num_sum + count
    count = count + 1 #
    if count== 5:
        break
print("Sum of first ",count,"integers is: ", num_sum)
