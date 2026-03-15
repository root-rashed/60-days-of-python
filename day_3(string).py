# INPUT
data = "data"
print(type(data))
data = input()
print(type(data))


# Type casting
x= int(input("Enter 1st num: "))
y = int(input("Enter 2nd num: "))
print("Result: ",x+y)



# Length
data = "60 days of python"
length = len(data)
x= data.count('python')
y =data.count('Days of')

print(length)
print(x)
print(y)



import sys
size= sys.getsizeof(data)
print(size) 

# ==================================================

# Find
# If not found print -1
print(data.find('of'))
print(data.find('f',10,15))  

# Index
print(data.index('y'))
print(data.index('y',5,10))


# Upper and lower case
print(data.upper())
print(data.lower())

x= "data science is fun"
print(x.capitalize())
print(x.casefold())

print(x.swapcase())
print(x.title())


print(x.isupper())
print(x.isdigit())
print(x.encode())
print(type(x.encode()))


x.split()
print(x.split()[0])



print(x.center(50))


x.replace('data','AI')
print(x.replace('data','AI'))



# Format
x= 100
y =100
z = x*y
print('I have ',z,'taka')
print('I have {} taka'.format(z))