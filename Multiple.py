
class Wheel:
    def feature_wheel(self):
        print("It has a circular wheel.")

class Rubber:
    def feature_rubber(self):
        print("It is made of rubber.")

class Tyre(Wheel, Rubber):
    def feature_tyre(self):
        print("This is a tyre made of rubber and shaped like a wheel.")

obj = Tyre()
obj.feature_wheel()  
obj.feature_rubber()   
obj.feature_tyre()     