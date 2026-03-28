#  Positional arguments
# Keyword arguments
# Default argumets
# Variable length arguments



# These are parameters
def add(x,y):
    return x+y
# positional arguments
print(add(10,20))



# Keyword arguments
def personal(job,income):
    print("Job: ",job)
    print("Income: ",income)
personal(income=1000000,job="AI Engineer")



# Default arguments
# Override
def personal(job,income=2000000):
    print("Job: ",job)
    print("Income: ",income)
personal(income=2000000,job="AI Engineer")



# Variable length
def add(x,*y):
    print(x)
    print(y)
    
add(10,20,30,40)