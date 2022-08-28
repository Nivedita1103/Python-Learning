c=int(input("Enter class obtained"))
s=int(input("number of subjects failed"))
if c==1:
    if s>3:
        print("no grace marks")
    elif s<=3:
        g=5
        print(" grace per subject:",g)
elif c==2:
    if s>2:
        print("no grace marks")
    elif s<=2:
        g=4
        print(" grace per subject:",g)
elif c==3:
    if s>1:
        print("no grace marks")
    elif s==1:
        g=5
        print(" grace per subject:",g)

        
