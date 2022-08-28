str = "Engineering" #looping and indexing
reversedString=[] #Empty list
index = len(str) # Update the index value using the length of the string, index=11
while index > 0: # 11,10,.....1,0
    reversedString += str[ index - 1 ] # reversedString=reversedString+string[0-1]
    index = index - 1 # index=10,9,8,7,6,5,4,3,2,index=1-1=0
print(reversedString)
