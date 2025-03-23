def printAllMathOperations(firstNumber, secondNumber):
    print(f"\nAddition: {firstNumber} + {secondNumber} = {firstNumber + secondNumber}")
    print(f"Subtraction: {firstNumber} - {secondNumber} = {firstNumber - secondNumber}")
    print(f"Multiplication: {firstNumber} * {secondNumber} = {firstNumber * secondNumber}")
    print(f"Division: {firstNumber} / {secondNumber} = {firstNumber / secondNumber}\n")

def convert(firstNumber, secondNumber):
    firstNumberInteger = int(firstNumber)
    secondNumberFloat = float(secondNumber)
    print(f"Float -> Integer: {firstNumberInteger}")
    print(f"Integer -> Float: {secondNumberFloat}\n")

def absoluteDifference(firstNumber, secondNumber):
    absoluteDifference = abs(firstNumber - secondNumber)
    print(f"Absolute difference -> {absoluteDifference}\n")

def isEven(number):
    if number % 2 == 0:
        print(f"{number} is even")
        return True
    print(f"{number} is odd")
    return False

firstNumber = float(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

printAllMathOperations(firstNumber, secondNumber)
convert(firstNumber, secondNumber)
absoluteDifference(firstNumber, secondNumber)
isEven(firstNumber)
isEven(secondNumber)