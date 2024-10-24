def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def calculator():
    print "Simple Calculator"
    print "1. Add"
    print "2. Subtract"
    print "3. Multiply"
    print "4. Divide"

    choice = raw_input("Enter choice (1/2/3/4): ").strip()  # Use raw_input in Python 2

    try:
        num1 = float(raw_input("Enter first number: "))  # Use raw_input
        num2 = float(raw_input("Enter second number: "))  # Use raw_input
    except ValueError:
        print "Invalid input! Please enter valid numbers."
        return

    if choice == '1':
        print "Result:", add(num1, num2)
    elif choice == '2':
        print "Result:", subtract(num1, num2)
    elif choice == '3':
        print "Result:", multiply(num1, num2)
    elif choice == '4':
        print "Result:", divide(num1, num2)
    else:
        print "Invalid Input"

if __name__ == "__main__":
    calculator()

