# write a python code for factorial of a number using functions

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number to calculate its factorial: "))
result = factorial(num)
print(f"The factorial of {num} is {result}.")

#write a python code for factorial of a number in one shot solution

num = int(input("Enter a number to calculate its factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")


