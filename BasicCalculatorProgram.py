# Ask the user to enter the first number and second number
number1 = float(input("Enter the first number: "))

number2 = float(input("Enter the second number: "))

# Ask the user to enter the operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation based on the user's input
if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    # Check for division by zero
    if number2 == 0:
        result = "Error: Division by zero is not allowed."
    else:
        result = number1 / number2
else:
    result = "Error: Invalid operation."

# The result
print(f"The result is: {result}")
