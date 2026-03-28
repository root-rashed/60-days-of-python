num =[1,2,3,4,5]
print(num)


sqr = list(map(lambda x:x**2,num))
print(sqr)


fil = list(filter(lambda num: num%2==1,num))
print(fil)


from functools import reduce
after_reduced = reduce(lambda a,b:a+b,num)
print(after_reduced)