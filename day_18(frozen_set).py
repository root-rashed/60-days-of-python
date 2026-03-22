sub = {"seu","cse","ai"}
sub1 = {"data","science"}

# Can't be modified
sub2 = frozenset(sub)

print(type(sub1))


sub2.union(sub1)
print(sub2)