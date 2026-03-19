# List methods
list =[11,2,3,42,5]
list.sort()
print(list)


list.reverse()
print(list)



list2 = list.copy()
print(list2)



list[0]=100
print(list)



list.append(200)
print(list)



# In list2 add all list elements
list2.extend(list)
print(list2)



list2.insert(0,'seu')
print(list2)


print(list2.index('seu'))
print(list2.index(2))
print(list2.count(200))



list2.remove(2)
print(list2)



list2.pop(-1)
print(list2)

# Delete
del list2[1]
print(list2)


# All clear
list2.clear()
print(list2)