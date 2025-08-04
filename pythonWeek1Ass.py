# Week 1 Python Assignment
# This script prompts the user to input two numbers and an arithmetic operation,
# then performs the operation and displays the result.

print("\nHello! and Welcome to my Python Week 1 Assignment.\nMy name is Ayanda Thomas Mbuyisa")

# Prompt the user to enter the first number
num1 = int(input("\nPlease Enter your first number: "))

# Prompt the user to enter the second number
num2 = int(input("\nPlease Enter your second number: "))

# Prompt the user to enter an arithmetic operation
operation = input("\nPlease enter an operation e.g (+ , - , * , /): ")

# Initialize a variable to store the result
answer = None

# Perform the selected operation
if operation == '+':  # Addition
    answer = num1 + num2

elif operation == '-':  # Subtraction
    answer = num1 - num2

elif operation == '*':  # Multiplication
    answer = num1 * num2

elif operation == '/':  # Division
    if num2 != 0:  # Prevent division by zero
        answer = num1 / num2
    else:
        print("Cannot divide by 0")

else:
    print("Invalid operation")

# Display the result if a valid operation was performed
if answer is not None:
    print(f"\nResult: {num1} {operation} {num2} = {answer}")
