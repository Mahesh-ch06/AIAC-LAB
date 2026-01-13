# Write a Python code that takes input from user and calculates the factorial of a number using a for loop...handles edge cases..give me code using functions
def calculate_factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, num + 1):
            factorial *= i
        return factorial
num = int(input("Enter a number to calculate its factorial: "))
result = calculate_factorial(num)
print(f"The factorial of {num} is {result}")

