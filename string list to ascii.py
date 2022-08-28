lt = ['cs', 'is', 'best'] 

print("The original list : " + str(lt)) 
 
res = [ord(ele) for sub in lt for ele in sub] 

print("The ascii list is : " + str(res)) 
