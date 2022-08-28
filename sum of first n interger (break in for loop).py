numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
sum = 0
count = 0
for x in numbers: #x=5
    sum = sum + x #15
    count = count + 1 #5
    if count == 5:
        break #go out of loop
print("Sum of first ",count,"integers is: ", sum)
   
   
   #Break in for loop
