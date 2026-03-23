import array as ar

# Array
ar1 = ar.array('i',[1,2,3,4,5])
print(ar1)


ar2 = ar.array('f',[1.5,2.5,3.5,4.5,5.5])
print(ar2)


print(ar2[0])
 

ar2[0] = 1.1
print(ar2[0])

ar2.append(6.5)
print(ar2)


del ar2[-1]



print(len(ar2))


ar2.reverse()
print(ar2)



print(ar1.count(1))
print(ar1.index(1))


ar1.pop()
print(ar1)

ar1.remove(4)
print(ar1)