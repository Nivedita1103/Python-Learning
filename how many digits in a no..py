n=int(input("enter a number from 0 to 999:"))
if n<0:
    print("invalid entry")
elif n<10:
    print("single digit number is entered")
elif n<100:
    print("2 digit number s entered")
elif n<=999:
    print("3 digit number entered")
else:
    print("invalid entry")
