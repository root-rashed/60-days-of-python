def user_input():
    x1 = int(input())
    x2 = int(input())
    x3 = int(input())
    x4 = int(input())
    return (x1,x2),(x3,x4)

r1,_ = user_input()
print(r1)



# One function call in another
def mul():
    x= int(input("Enter x: "))
    y= int(input("Enter y: "))
    result = x*y
    return result

def mul1():
    res = mul()
    z= int(input("Enter z: "))
    final = res*z
    return final

fn = mul1()
print("Final result is: {}".format(fn))