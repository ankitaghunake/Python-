Names= set(["Ankita","Darshana","Divya","Revaa","Maithili","Madhushri"])
print(type(Names))
print(Names)
#functions
Names.add("Sanaa")
print(Names)
Names.update("Ankita")
print(Names)
Names.discard("Darshana")
print(Names)
Names.remove("Divya")
print(Names)
Names.pop()
print(Names)
Names.copy()
print(Names)
Names.clear()
print(Names)

#Operations on two sets
A1 ={72,59,34,57,135,99} #Anpther way of representing sets
print(A1)
A2 ={100,43,59,12,135,1111,72}
print(A2)
#Union
print(A1 | A2)
#Another way for union operation
print(A1.union(A2))
print(A1.intersection (A2))
print(A1.difference(A2))
print(A1.symmetric_difference(A2))
print(A1.isdisjoint(A2))
print(A2.issubset(A1))
print(A2.issuperset(A1))