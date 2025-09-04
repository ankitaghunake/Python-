with open('example.txt','w')as file:
 file.write("Ankita G\n")
 file.write("I can do everything....\n")

with open('example.txt','r')as file:
  print(file.read())

  file.seek(6)
  print(file.read())

with open('example.txt','a') as file:
    file.write("Appended line...\n")
 
with open('example.txt','r+')as file:
  print(file.read())


with open('example.txt','r')as file:
  lines=file.readlines()
  print("Readlines: ",lines)
  
with open('example.txt','r')as file:
  line=file.readline()
  print("Readline: ",line)