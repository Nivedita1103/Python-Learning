def Reverse_Integer(Number):
    Reverse = 0
    
    while(Number > 0): #iterative task
        Reminder = Number %10
        Reverse = (Reverse *10) + Reminder

        Number = Number //10
    return Reverse
    
Number = int(input("Please Enter any Number: "))
Reverse = Reverse_Integer(Number) # Recursive Calling is Here Guys
print("\n Reverse of entered number is = %d" %Reverse)
