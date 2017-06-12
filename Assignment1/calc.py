import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y==0:
        return "Can't divide with 0 "
    return x / y

# take input from the user


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = int(input("Enter choice(1/2/3/4):"))

if choice>1 and choice<5:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

else:
    print("Invalid Input")
    sys.exit()

if choice == 1:
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == 2:
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == 3:
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == 4:
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")