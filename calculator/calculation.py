# This program performs basic arithmetic operations based on user input

# Display the available operations to the user
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take the user's choice of operation as input
choice = input("Enter choice: ")

# Take two numbers as input from the user and convert them to integers
num1 = int(input("Enter the first number: "))  # Convert input to integer
num2 = int(input("Enter the second number: "))  # Convert input to integer

# Define a function to add two numbers
def add(x, y):
    return x + y

# Define a function to subtract one number from another
def subtract(x, y):
    return x - y

# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

# Define a function to divide one number by another
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Perform the corresponding operation based on user input
if choice == '1':
    # If choice is 1, perform addition
    print("The sum is " + str((num1) + (num2)))
elif choice == '2':
     # If choice is 2, perform subtraction
    print("The difference is " + str((num1) - (num2)))
elif choice == '3':
    # If choice is 3, perform multiplication
    print("The product is " + str((num1) * (num2)))
elif choice == '4':
    # If choice is 4, perform division
    result = divide(num1, num2)
    # Check if the result is an error message or a valid division result
    if isinstance(result, str):
        print(result)
    else:
        print("The result is " + str((num1) / (num2)))
else:
    # If the user enters an invalid choice, display an error message
    print("Invalid input")
