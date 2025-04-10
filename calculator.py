if __name__ == "__main__":

n1 = input("Enter your first number")
n2 = input("Enter your secoond number")
operation = input("Enter the operation you want to perform (+, -, * and /)")

def addition(n1,n2):
  return float(n1) + float(n2)

def subtraction(n1,n2) :
  return float(n1) - float(n2)

def multiplication(n1,n2):
  return float(n1) * float(n2)

def division(n1,n2):
  return float(n1) / float(n2)

if (operation == "+"):
  print(addition(n1, n2))

elif (operation == "-"):
  print(subtraction(n1, n2))

elif (operation == "*"):
  print(multiplication(n1, n2))

else:
  print(division(n1, n2))