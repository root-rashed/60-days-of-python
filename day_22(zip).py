name =['rashed','sabit','prio']
varsity = ['seu','eub','isd']
zipped = dict(zip(name,varsity))


print(zipped)
print(type(zipped))

print(zipped.keys)
print(zipped.values())


name1,varsity1 = zip(*zipped)
print(name1)
print(varsity1)