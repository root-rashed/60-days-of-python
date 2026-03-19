squares = [x**2 for x in range(10)]
print(squares)


# Condition
evens = [x for x in range(10) if x%2 == 0]
print(evens)



matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)



words = ['python','list','ai','data','science']
lengths = [len(word) for word in words]
print(lengths)