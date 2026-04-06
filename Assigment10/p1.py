#......................................
# File Name: p1.py
#.......................................
def factorial(n):
    if n == 0:
        return 1 # Factorial of 0 is defined to be 1
    else:
        return n * factorial(n - 1) # Recursive call to calculate factorial of n-1