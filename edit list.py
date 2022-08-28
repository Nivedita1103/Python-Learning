def myfunc(mylist):
    print("\t Inside CALLED Function now")
    print("\t List recieved:",mylist)
    mylist.append(2)
    mylist.extend([5,1])
    print("\t List after adding some elements:",mylist)
    mylist.remove(5)
    print("\t List within called function,after all changes:",mylist)
    return
list1=[1]
print("List before function call:",list1)
myfunc(list1)
print("\List after function call:",list1)
