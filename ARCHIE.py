import time

def countdown():
    for i in range(10,0,-1):
        print(f"Countdown {i}")
        time.sleep(1)
countdown()
print("YOU HAVE BEEN HACKED")

# Program make a simple calculator

# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

print("Select operation.")
print("2.Subtract")


# Take input from the user 
choice = input("Enter 2: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
