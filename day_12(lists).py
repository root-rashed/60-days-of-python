ls =[1,2,3,4,5]
print(ls)

ls.append('6')
print(ls)

import sys
print(sys.getsizeof(ls))

ls.pop()
print(ls)


# User input
list =[]
n= int(input("Enter total number: "))
for i in range(n):
    new =input()
    list.append(new)
    print(list)

