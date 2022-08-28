import bisect
mylist=[10,20,30,40,50,60,70]
print("the list in sorted order is")
print(mylist)
ITEM=int(input("Enter new element to be inserted :"))
ind=bisect.bisect(mylist,ITEM)
bisect.insort(mylist,ITEM)
print(ITEM,"inserted at index",ind)
print("the list after inserting new element is")
print(mylist)
