
#public 
#simple class , object , default constructor creation
class demo:
    var1 ='Hii'
    def __init__(self):
      self.str="Welcome.."
    def display(self):
      print(self.var1)
      print(self.str)
      
    
obj = demo()
obj.display()
   
#parametrized constructor
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


#Destructor 

class Employee:
   def __init__(self):
      print("Employee Created..")
   def __del__(self):
      print("Destructor called,Employee deleted")
obj= Employee()
del obj