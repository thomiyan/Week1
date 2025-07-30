# week 1 python assignment

userName = input("\nHello! Welcome. Please enter your first name: ")
print("\nHello! ", userName, ". Welcome to my week 1 python assignment.\n My name is Thomas")

# first number input
num1 = int(input("\nPlease Enter your first number: "))

# second number input
num2 = int(input("\nPlease Enter your second number: "))

# operation input
operation = input("\nPlease enter am operation e.g (+ , - , * , /) ")

# check the operation validity and perform the operation if valid
if operation == '+': # check if operation is plus (+)
    answer = num1 + num2

elif operation == '-': # check if operation is minus (-)
    answer = num1 - num2

elif operation == '*':  # check if operation is multiplication (*)
    answer = num1 * num2

elif operation == '/':  # check if operation is divide (/)
   
    if num2 != 0:  # check if second number is not equal to 0
        answer = num1 / num2
    else:
        print("Can not divide by 0")

else:
    print("Invalid operation")

# if all goes well, system prints the results
print(f"{num1} + {num2} = {answer}")



