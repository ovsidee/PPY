def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by 0!"
    return a / b

def squareRoot(number):
    return number ** 0.5

def power(a, b):
    return a ** b

while True:
    print("\nWelcome To Calculator!")
    print("Type 1 to add numbers:")
    print("Type 2 to subtract numbers:")
    print("Type 3 to multiply numbers:")
    print("Type 4 to divide numbers:")
    print("Type 5 to square root number:")
    print("Type 6 to power numbers:")
    print("Type 7 to exit calculator:")

    try:
        command = int(input("\nEnter the command: "))
    except ValueError:
        print("\nPlease enter a number.")
        continue

    match command:
        case 1 | 2 | 3 | 4 | 6:
            firstNumber = float(input("Enter the first number: "))
            secondNumber = float(input("Enter the second number: "))

            if command == 1:
                print(f"Result: {addition(firstNumber, secondNumber)}")
            elif command == 2:
                print(f"Result: {subtraction(firstNumber, secondNumber)}")
            elif command == 3:
                print(f"Result: {multiplication(firstNumber, secondNumber)}")
            elif command == 4:
                print(f"Result: {division(firstNumber, secondNumber)}")
            elif command == 6:
                print(f"Result: {power(firstNumber, secondNumber)}")
        case 5:
            number = float(input("Enter the number to square root: "))
            if number < 0:
                print(f"{number} is negative, cannot calculate square root!")
            else:
                print(f"Result: {squareRoot(number)}")
        case 7:
            print("Thank you! Bye bye...")
            quit(0)
        case _:
            print("Invalid input, please try again!")

#1
# If the user tries to divide by 0, the function(division) returns "Cannot divide by 0!" instead of crashing.
# This message is displayed to the user, preventing a math error. otherwise it divides without any issues.

#2
# command = int(input("\nEnter the command: ")) -> Converts input to an integer.
# firstNumber = float(input("Enter the first number: ")) -> Converts input to a floating-point number.
# secondNumber = float(input("Enter the second number: ")) -> Converts input to a floating-point number.
# number = float(input("Enter the number to square root: ")) -> Converts input to a floating-point number.
# int is used for command because it's selecting an option from the menu.
# float is used for calculations since numbers can be decimals (e.g. 5.5).

#3
# If the user enters letters or symbols instead of a number, the program does not crash.
# Instead, it prints "Please enter a number." and restarts the loop, prompting the user again.
# and additionally:
# case _:
#   print("Invalid input, please try again!")
# If the user enters a number not in the menu (e.g., 8, 9, 100), they get a message and can try again.