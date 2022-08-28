num = input("insert a number of your choice ")
rev = ''
for i in range(len(num), 0, -1):
     rev += num[i-1]
print(int(rev))
