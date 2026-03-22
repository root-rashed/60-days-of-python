sub = {1,2,3,4,5}
sub1 = {1,2,3}


# Can't be modified
sub2 = frozenset(sub1)


sub1.add(1)
print(sub1)


sub3 = sub2.copy()
print(sub3)


sub1.remove(1)
print(sub1)



sub.difference_update(sub3)
print(sub)


print(sub1.issubset(sub))
print(sub.issubset(sub1))

print(sub1.issuperset(sub))