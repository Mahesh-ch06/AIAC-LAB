'''Genrate a function that return fibonacci series of n terms with assert statement to check the functionality of the function.'''
def FibonacciGenerator(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        for i in range(2, n):
            next_term = fib_series[i - 1] + fib_series[i - 2]
            fib_series.append(next_term)
        return fib_series
assert FibonacciGenerator(0) == []
assert FibonacciGenerator(1) == [0]
assert FibonacciGenerator(2) == [0, 1]
assert FibonacciGenerator(5) == [0, 1, 1, 2, 3]
assert FibonacciGenerator(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
try:
    FibonacciGenerator(-3)
except ValueError as e:
    print(e)  # Output: Input must be a non-negative integer.
print("All assertions passed successfully.")