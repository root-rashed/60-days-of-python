# Numerical data
x= 10
y =20.5
z = 10+5j

print(type(x))
print(type(y))
print(type(z))


print(isinstance(z,complex))


# Type casting
n= float(x)
print(type(n))

# Integer to complex
n= complex(n)
print(n)

x = True
print(x)


# List
list = [1,2,3,True,[1,3],'data']
print(list[0])

# Tuple
t = (1,2,3,4,5,6)
print(t[0])
print(type(t))

# Range
x = range(5,10)
y = range(1,10,2)
z = range(10,1,-2)
print(x)

for i in x:
    print(i)

for i in y:
    print(i)

for i in z:
    print(i)


# Array
import array as ar
a= ar.array('i',[2,3,4,5])
print(a)
 

#  Set
s= {1,2,3,4,5}
print(s)


# Dictionary
dic = {'varsity':'seu',
       'dept': 'cse'}
print(dic)
print(dic.values())


# Data frame
# import pandas as pd
# df = pd.read_csv("read.csv")
# df.shape
# df.info()


# Binary types
byte_type = bytearray('abcde','utf-8')
print(byte_type)
 
print(memoryview(byte_type))