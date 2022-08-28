def isempty(stk):
    if stk==[]:
        return True
    else:
        return False
def push(stk,item):
    stk.append(item)
    top=len(stk)-1
def pop(stk):
    if isempty(stk):
        return "underflow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item
Stack=[]
top=None
while True:
    print("STACK OPERATIONS")
    print("1. Push")
    print("2.Pop")
    ch=int(input("enter your choice(1-3):"))
    if ch==1:
        item=int(input("enter item:"))
        push(Stack,item)
    elif ch==2:
        item=pop(Stack)
        if item=="underflow":
            print("underflow!Stack is empty!")
        else:
            print("popped item is",item)
    elif ch==3:
        break
else:
    print("invalid choice!")
    
