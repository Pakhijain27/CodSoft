#Available arithmetc operations to the user
print("Addition - 1")
print("Subtraction - 2")
print("Multiplication - 3")
print("Division - 4")

# Ask the user to choose the operation by choosing the numbers (1-4)
choice = int(input("Choose the operation: "))

# Check if the choice is a valid option (1-4)
if (choice in(1,2,3,4)):
  # if the choice is valid then promt the user to enter two numbers
  num1 = float(input("enter first number: "))
  num2 = float(input("enter second number: "))

# Perform the operation based on the user's choice
if choice == 1:
  #Addition Operation
  print("Answer = ",num1+num2)

elif choice == 2:
  #Addition Operation
  print("Answer = ",num1-num2)

elif choice == 3:
  #Addition Operation
  print("Answer = ",num1*num2)

elif choice == 4:
  #Addition Operation
  print("Answer = ",num1/num2)

# If the user enters an invalid operation number, print an error message
else:
  print("Invalid choice")
