def add (a,b=None):
    if b is not None:
        return a+b
    else:
        return a+10
print(add(5,2))
print(add(3))