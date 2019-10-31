End=True

while End == True:
  richter = float (input("Enter the Richter scale value. if you type -99 it will kill the program:"))
  if richter == -99:
    break
    while richter < 0:
        richter = float(input("Please enter a valid number: "))
  if(richter >= 8.0):
      print("Most structures will fall")
      continue
  elif (richter >= 7.0):
    print("Many buildings will be destroyed")
    continue
  elif (richter >= 6.0):
    print("Most buildings will be considerably damaged, some collapse")
    continue 
  elif (richter >= 4.5):
    print("Damage too poorly constructed buildings")
    continue
  elif (richter > 0):
    print("No destruction of buildings")
     
  else:
    print("The value must be greater than 0 enter another value")
    continue
