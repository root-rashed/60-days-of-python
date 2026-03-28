# Lamdha function

a = lambda x,y: x+y
print(a(1,2))

b = lambda x,y: x-y
print(b(1,2))

c = lambda x,y: x*y
print(c(1,2))


d = lambda x,y: x/y
print(d(1,2))




def operation_higher(x,y,operation):
    return operation(x,y)

# So the main point, when lamdha is the argument it usually assign operation = lambda x,y:x*y and return value
print(operation_higher(4,5, lambda x,y:x*y))