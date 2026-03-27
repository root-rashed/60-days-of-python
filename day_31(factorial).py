def fact(x):
    result =1

    if x ==0 or x == 1:
        return 1
    else:
        for i in range(x):
            result = result*(i+1)
        return result

print(fact(3))
print(fact(1500))