import array as arr


a= arr.array('i',[1,2,3,4])
print("The new created array is:",end=" ")
for i in range(0,4):
    print (a[i],end=" ")
print("\n")
#Double array
b= arr.array('d',[2.5,3.2,3.3])
print("The double array is:",end=" ")
for j in range(0,3):
    print (b[j],end=" ")
print("\n")

a.insert(1,5)    
print("Array after insertion: ",end=" ")
for i in (a):
    print(i,end=" ")
print("\n")

a.remove(2)    
print("Array after remove: ",end=" ")
for i in (a):
    print(i,end=" ")
print("\n")

b.append(2.8)    
print("Array after append: ",end=" ")
for j in (b):
    print(j,end=" ")
print("\n")

c=a.count(3)
print("count of 3: ",c ,end=" ")
print("\n")

b.pop(2)
print("Array after poping 3.3: ",end=" ")
for j in (b):
    print(j,end=" ")
print("\n")

d= a.index(3)
print("index of 3: ",d,end=" ")
print("\n")

a.reverse()
print("Array after reversing: ",end=" ")
for i in (a):
    print(i,end=" ")
print("\n")

a.clear()
print("Array after clear: ")
print("\n")
b.clear()
print("Array after clear: ")
print("\n")




