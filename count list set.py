def countl(l): #list elemnts are passed
    s=set(l) #collected list elements in sequence of set
    for i in s: # for all elements of the set sequence
        count=0
        for j in l: #for all input elements in list
            if (j==i): # same or not (input == sequenced elements of a set s)
                count=count+1
        print(f"item {i} occurs {count} times")
        print(i)
n=list(input("enter values").split(' ')) #list data type
countl(n)


