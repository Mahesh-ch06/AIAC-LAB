# Write a Python code that takes input from user and calculates the factorial of a number using iterative approach

def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

num = int(input("Enter a number to calculate its factorial: "))
factorial_result = factorial_iterative(num)
print(f"The factorial of {num} is {factorial_result}") 

# write a python code that takes input from user and calculates the factorial of a number using recursive approach
def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    
    else:
        return n * factorial_recursive(n - 1)
num = int(input("Enter a number to calculate its factorial: "))
factorial_result = factorial_recursive(num)
print(f"The factorial of {num} is {factorial_result}")







