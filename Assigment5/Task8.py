# genrate well commentes code to Check Prime Number
def is_prime_naive(n):
    """Check if a number is prime using the naive approach."""
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# Optimized Approach to Check Prime Number
def is_prime_optimized(n):
    """Check if a number is prime using the optimized approach."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number to check if it's prime: "))
    
    # Using Naive Approach
    if is_prime_naive(number):
        print(f"{number} is a prime number (Naive Approach).")
    else:
        print(f"{number} is not a prime number (Naive Approach).")
    
    # Using Optimized Approach
    if is_prime_optimized(number):
        print(f"{number} is a prime number (Optimized Approach).")
    else:
        print(f"{number} is not a prime number (Optimized Approach).")
# Analysis:
# Time Complexity:
# Naive Approach: O(n) - In the worst case, we check all numbers from 2 to n-1.
# Optimized Approach: O(√n) - We only check up to the square root of n and skip even numbers after checking for 2 and 3.
# The optimized approach significantly reduces the number of iterations needed to determine if a number is prime, especially for large values of n.
# Space Complexity:
# Both approaches have a space complexity of O(1) as they use a constant amount of space.