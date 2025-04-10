
def addition(n1,n2):
  return float(n1) + float(n2)

def subtraction(n1,n2) :
  return float(n1) - float(n2)

def multiplication(n1,n2):
  return float(n1) * float(n2)

def division(n1,n2):
  return float(n1) / float(n2)

if __name__ == "__main__":
  while True:
    try:
        n1 = float(input("Enter your first number: "))
        break 
    except ValueError:
        print("Invalid input. Please enter a number.")
  while True:
    try:
        n2 = float(input("Enter your second number: "))
        break 
    except ValueError:
        print("Invalid input. Please enter a number.")
operation = input("Enter the operation you want to perform (+, -, * and /) ")
valid_operations = ["+", "-", "*", "/"]


if (operation == "+"):
  print(addition(n1, n2))

elif (operation == "-"):
  print(subtraction(n1, n2))

elif (operation == "*"):
  print(multiplication(n1, n2))

elif (operation == "/"):
  print(division(n1, n2))

elif operation not in valid_operations:
    print("Invalid operation. Please try again.")
