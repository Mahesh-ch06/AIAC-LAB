# Write a Python code that takes input from user and calculates the factorial of a number using a for loop...without using any functions...optimize this code

num = int(input("Enter a number to calculate its factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print(f"The factorial of {num} is 1")
else:
    factorial = 1
    for i in range(2, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
