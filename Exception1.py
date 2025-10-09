class InvalidAgeException(Exception):
    pass
 

try :
      num = int(input("Enter a number: "))
      number = 18
      if num < number :
           raise InvalidAgeException
      else:
           print("Eligible to vote")

except InvalidAgeException:
     print("Exception Occured: Invalid age")
       