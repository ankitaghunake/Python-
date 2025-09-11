

class demo:
    var1 ='Hii'
    def __init__(self):
      self.str="Welcome.."
    def display(self):
      print(self.var1)
      print(self.str)

      
class para:
   var2 ="Hello"
   def __init__(self,name,age):
      self.name = name
      self.age = age
      self.str = "World"
   def display(self):
      print(self.var2) 
      print(self.str)
     
      print(f"name:{self.name}")
      print(f"age:{self.age}")
obj =para("Ankita",20)
obj.display()

class Employee(demo):


    obj = demo()
    obj.display()