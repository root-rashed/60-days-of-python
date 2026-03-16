dept = ['cse','eee','math']
for x in dept:
    print(x)


print('############################################')
for i in range(-100,-9,1):
    print(i)


print("############################################")
sum =0
for i in range (10,20,1):
    if (i%3!=0) and (i%5!=0) and (i%7!=0) and (i%2!=0):
        sum+=i
print(sum)


print("############################################")
# Without heavy logic
x = int(input("Enter a number: "))
fact= x
for i in range(x,2,-1):
    fact = fact*(i - 1)

print('Factorial of {} is: {} '.format(x,fact))