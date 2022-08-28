string1 = input("Enter the first string: ") 
print(string1, end = "\n")

string2 = input("Enter the second string: ") 
print(string2, end ="\n") 
 
if (string1 == string2) :
    print("both strings are same")
    def reverse(s): 
            if len(s)==0:
                return s
            else:
                return reverse(s[1:]) + s[0]
    s= string1 
    print ("reversed string: ",reverse(s)) 
else :
    print("strings are different")
    def reverse(s): 
            if len(s)==0:
                return s
            else:
                return reverse(s[1:]) + s[0]
    s= string2 
    print ("reversed string: ",reverse(s)) 
		
