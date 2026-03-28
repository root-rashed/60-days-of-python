# def web():
#     print("Data")
#     web()

# web()


def factor(x):
    if x==0:
        return 1
    return x*factor(x-1)

print("Factorial: ",factor(5))