import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    return math.sqrt(a)

while True:
    print("\n==== ADVANCED CALCULATOR ====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (x^y)")
    print("6. Square Root")

    choice = input("Enter your choice (1-6): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))

        elif choice == '2':
            print("Result:", sub(num1, num2))

        elif choice == '3':
            print("Result:", mul(num1, num2))

        elif choice == '4':
            print("Result:", div(num1, num2))

        elif choice == '5':
            print("Result:", power(num1, num2))

    elif choice == '6':
        num = float(input("Enter number: "))
        print("Result:", sqrt(num))

    else:
        print("Invalid choice")

    again = input("Do you want to continue? (yes/no): ")
    if again.lower() != 'yes':
        print("Calculator closed.")
        break

input("Press Enter to exit...")