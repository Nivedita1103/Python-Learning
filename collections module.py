import collections #module
a=["a","b","c","a"]
o=collections.Counter(a) #Counter function in collections module
print(o)
for i in o:
    print("element",i ,"occurs", o[i])
