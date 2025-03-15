#Operations (+,-,/,**,//)
def simple_calculator():
    """
    A simple calculator that takes two numbers and an operation as input
    and prints the result.
    """
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == '+':
            result = a + b
            print(f"{a} + {b} = {result}")
        elif operation == '-':
            result = a - b
            print(f"{a} - {b} = {result}")
        elif operation == '*':
            result = a * b
            print(f"{a} * {b} = {result}")
        elif operation == '/':
            if b == 0:
                print("Error: Does not exist.")
            else:
                result = a / b
                print(f"{a} / {b} = {result}")
        else:
            print("Invalid operation. Please enter +, -, *, or /.")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    simple_calculator()