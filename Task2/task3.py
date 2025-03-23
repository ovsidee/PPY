import math

def findAllPrimeNumbers(firstNumber, secondNumber):
    res = []
    for numberBetweenTwo in range(firstNumber, secondNumber + 1):
        if numberBetweenTwo > 1:
            for j in range(2, int(math.sqrt(numberBetweenTwo) + 1)):
                if numberBetweenTwo % j == 0:
                    break
            else:
                res.append(numberBetweenTwo)
    return res

firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

allPrimeNumbers = findAllPrimeNumbers(firstNumber, secondNumber)

print(f"All prime numbers in range {firstNumber} to {secondNumber} are: {allPrimeNumbers}")
print(f"Their average: {sum(allPrimeNumbers)/len(allPrimeNumbers)}")
print(f"Their sum: {sum(allPrimeNumbers)}")