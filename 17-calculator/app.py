def add(x, y):
    return x+y


def subtract(x, y):
    return x - y


def multipy(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error Division by zero is not allowed."
    return x / y


def main():
    print("\n==== SIMPLE CALCULATOR")
    print("Select operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("\nEnter choice (1-4): ")
        if choice not in ("1", "2", "3", "4"):
            print("\nPlease enter a number from 1 -4")
        else:
            break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌Error! Please enter a valid number")
        return

    if choice == "1":
        print(f"\n{num1} + {num2} = {add(num1, num2)}")
    elif choice == "2":
        print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == "3":
        print(f"\n{num1} x {num2} = {multipy(num1, num2)}")
    elif choice == "4":
        print(f"\n{num1} / {num2} = {divide(num1, num2)}")

    again = input(
        "\nDo you want to perform another calculation (yes/no): ").lower()
    if not again.startswith("y"):
        print("GoodBye")
        return
    else:
        main()


main()
