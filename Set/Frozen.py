
#Frozen set
fs1=frozenset([1,2,3,4,5,6])
fs2={45,6,2,88,}
print(type(fs1))
for i in fs1:
    print (i);
#Functions
fs1.copy()
print(fs1)
fs2.copy()
print(fs2)
print(fs1.difference(fs2))
print(fs2.difference(fs1))
print(fs1.union(fs2))
print(fs2.union(fs1))
print(fs1.intersection(fs2))
print(fs2.intersection(fs1))
print(fs1.isdisjoint(fs2))
print(fs2.isdisjoint(fs1))
print(fs1.issubset(fs2))
print(fs2.issubset(fs1))
print(fs1.issuperset(fs2))
print(fs2.issuperset(fs1))
print(fs1.symmetric_difference(fs2))
print(fs2.symmetric_difference(fs1))
print(fs1.__and__(fs2))
print(fs2.__and__(fs1))
print(fs1.__or__(fs2))
print(fs2.__or__(fs1))