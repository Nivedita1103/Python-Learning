info={'riya':'CSc.','mark':'eco','ishpreet':'eng','kamaal':'Env.Sc'}
inp=input("enter value to be searched for:")
if inp in info.values():
    for a in info:
        if info[a]==inp:
            print("The key of given value is",a)
            break
        else:
            print("given value does not exist in dictionary")
