list1=[12,34,56.9,"india","coolest",3450]
list2=[100,200,300,"water"]
print(list1+list2)
print(list1[2]+list2[2])
print(list1[1:4])
print(list2*3)
m1= "india" in list1
print(m1)
m2= 1000 not in list2
print(m2)
list1.insert(3,12000) #inserting 12000 in 3rd index
print(list1)
list2[2]=20 # replacing index 2 of list to 20
print(list2)
list2[3]=10000
print(list1)
list1.remove(34)
print(list1)
list2.remove(list2[1])
print(list2)

