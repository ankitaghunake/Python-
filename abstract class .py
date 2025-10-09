from abc import ABC
class car(ABC):
    def mileage(self):
     pass

class Tesla(car):
   def mileage(self):
      print("The mileage is 30 kmph")

class suzuki(car):
   def mileage(self):
        print("The mileage is 60 kmph")

t = Tesla()
t.mileage()
s = suzuki()
s.mileage()