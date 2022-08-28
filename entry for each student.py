count=int(input("how many students are there in class?"))
fileout=open("marks.dat","w")
for i in range(count):
    print("enter details for student",(i+1),"below:")
    rollno=int(input("rollno:"))
    name=input("name:")
    marks=float(input("marks:"))
    rec=str(rollno)+","+name+","+str(marks)+'\n'
    fileout.write(rec)
fileout.close()
