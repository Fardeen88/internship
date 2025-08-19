# calculator.py
while True:
    print("\n--- Simple Calculator ---")
    print("Enter 'q' to quit")

    num1 = input("Enter first number: ")
    if num1.lower() == 'q':
        break
    num1 = float(num1)

    operator = input("Enter operator (+, -, *, /): ")

    num2 = input("Enter second number: ")
    if num2.lower() == 'q':
        break
    num2 = float(num2)

    if operator == "+":
        print(f"Result: {num1 + num2}")
    elif operator == "-":
        print(f"Result: {num1 - num2}")
    elif operator == "*":
        print(f"Result: {num1 * num2}")
    elif operator == "/":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero")
    else:
        print("Invalid operator")
