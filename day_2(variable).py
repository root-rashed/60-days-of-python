x=100
y=100

# Stored in same memory adress
print(id(x))
print(id(y))

def fun1():
    # Local
    x=500 
    print("My num is: ",x)

def fun2():
    # Global
    print("My num is: ",y)


# Call the function
fun1()
fun2()
