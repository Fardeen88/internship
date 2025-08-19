# week1_menu_app.py

def even_odd_checker():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")


def multiplication_table():
    num = int(input("Enter a number: "))
    limit = int(input("Enter the range: "))
    for i in range(1, limit + 1):
        print(f"{num} x {i} = {num * i}")


def positive_negative_zero():
    num = int(input("Enter a number: "))
    if num > 0:
        print(f"{num} is Positive")
    elif num < 0:
        print(f"{num} is Negative")
    else:
        print("Zero entered")


def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

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


# -------- Main Menu --------
while True:
    print("\n====== Week 1 Menu App ======")
    print("1. Even/Odd Checker")
    print("2. Multiplication Table")
    print("3. Positive/Negative/Zero Checker")
    print("4. Calculator")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        even_odd_checker()
    elif choice == "2":
        multiplication_table()
    elif choice == "3":
        positive_negative_zero()
    elif choice == "4":
        calculator()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
