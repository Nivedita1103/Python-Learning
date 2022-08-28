m1=int(input("enter percent in s1"))
m2=int(input("enter percent in s2"))
if m1>=55 and m2>=45:
    print("Pass")
elif 45<=m1 and m1<=55 and  m2>=55:
    print("pass")
elif m1>=65 and m2<=45:
    print("you may reappear")
else:
    print("Fail")
