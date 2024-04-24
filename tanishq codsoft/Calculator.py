import time  # Import the time module for time.sleep()

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def calculator():
    print("\033[1;31mSelect operation:\033[0m")
    print("\033[1;32m1. Add\033[0m")
    print("\033[1;32m2. Subtract\033[0m")
    print("\033[1;32m3. Multiply\033[0m")
    print("\033[1;32m4. Divide\033[0m")

    while True:
        try:
            choice = int(input("\033[1;31mEnter your choice (1/2/3/4): \033[0m"))
            if choice in [1, 2, 3, 4]:
                break
            else:
                print("\033[1;31mInvalid input. Please enter a number between 1 and 4.\033[0m")
        except ValueError:
            print("\033[1;31mInvalid input. Please enter a number between 1 and 4.\033[0m")

    num1 = float(input("\033[1;31mEnter first number: \033[0m"))
    num2 = float(input("\033[1;31mEnter second number: \033[0m"))

    if choice == 1:
        print("\033[1;31m" + str(num1) + " + " + str(num2) + " = ", end="")
        time.sleep(1)
        print(add(num1, num2))
    elif choice == 2:
        print("\033[1;31m" + str(num1) + " - " + str(num2) + " = ", end="")
        time.sleep(1)
        print(subtract(num1, num2))
    elif choice == 3:
        print("\033[1;31m" + str(num1) + " * " + str(num2) + " = ", end="")
        time.sleep(1)
        print(multiply(num1, num2))
    elif choice == 4:
        try:
            print("\033[1;31m" + str(num1) + " / " + str(num2) + " = ", end="")
            time.sleep(1)
            print(divide(num1, num2))
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    calculator()
