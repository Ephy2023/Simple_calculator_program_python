# Simple calculator program in Python

# Function to perform the operation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation!"

# Main program
try:
    # Taking user inputs
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Calculating the result
    result = calculate(num1, num2, operation)

    # Printing the result
    if isinstance(result, str):  # To check if the result is an error message
        print(result)
    else:
        print(f"{num1} {operation} {num2} = {result}")

except ValueError:
    print("Invalid input! Please enter numeric values for the numbers.")
