ids =(1,2,3)
name =('rashed','sabit','gifary')

zipped = tuple(zip(ids,name))
print(zipped)

ids_new,name_new = zip(*zipped)
print(ids_new)
print(name_new)


# Unpacking using loop
for ids,names in zipped:
    print(ids,names)

# Enum
for data in enumerate(zipped):
    ids,name = data
    print(data)


for index,pair in enumerate(zipped):
    ids,name = pair
    print(index,ids,name)