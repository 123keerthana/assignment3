#Name:Keerthana
#Assignment 3
#code of simple calculator

print ("Select an operation to perform:")
print("1 -Addition")
print("2-Subtraction")
print("3-Multiplication")
print("4-Division")

operation=input()

if operation=="1":
  num1=int(input("Enter the num1:"))
  num2=int(input("Enter the num2:"))
  print("The sum is",num1+num2)
  #code for add
elif operation=="2":
  num1=int(input("Enter the num1:"))
  num2=int(input("Enter the num2:"))
  print("The sub is",num1-num2)
  #code for sub
elif operation=="3":
  num1=int(input("Enter the num1:"))
  num2=int(input("Enter the num2:"))
  print("The mul is",num1*num2)
  #code for mul
elif operation=="4":
  num1=int(input("Enter the num1:"))
  num2=int(input("Enter the num2:"))
  print("The div is",+num1 / num2)
   #code for div
else:
  print("Invalid Entry")
  
  #thank you 
