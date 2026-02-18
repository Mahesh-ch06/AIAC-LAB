def FactorialGenerator(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
assert FactorialGenerator(5) == 120
assert FactorialGenerator(0) == 1
assert FactorialGenerator(1) == 1
try:
    FactorialGenerator(-3)
except ValueError as e:
    print(e)  # Output: Input must be a non-negative integer.
print("All assertions passed successfully.")