def binsearch(ar,key,low,high):
    if low>high:
        return -999
    mid=int((low+high)/2)
    if key==ar[mid]:
        return mid
    elif key<ar[mid]:
        high=mid-1
        return binsearch(ar,key,low,high)
    else:
        low=mid+1
        return binsearch(ar,key,low,high)
ary=[2,20,50,1,33,90,1,10,100]

item=int(input("enter search item:"))
res=binsearch(ary,item,0,len(ary)-1)
if res>=0:
    print(item,"found at index",res)
else:
    print("sorry!",item,"not found in array")
