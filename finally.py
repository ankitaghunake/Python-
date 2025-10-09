class ZeroDivisionError(Exception):
    pass
 
 
try :
      
      n= int(input("Enter value of n: "))
      res = (100/n)
      

except ZeroDivisionError:
     print("You can't divide by zero...")
     raise ZeroDivisionError

else:
     print("Result is : ",res)

finally:
     print("Exception completed...")