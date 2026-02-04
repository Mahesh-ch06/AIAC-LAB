#genrate well commentes code for fibonacci series using recursion
def fibonacci(n):
    """Generate Fibonacci series up to n terms using recursion."""
    # Base cases
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        next_value = fib_series[-1] + fib_series[-2]
        fib_series.append(next_value)
        return fib_series
# Example usage
if __name__ == "__main__":
    terms = int(input("Enter the number of terms for Fibonacci series: "))
    series = fibonacci(terms)
    print(f"Fibonacci series up to {terms} terms: {series}")
