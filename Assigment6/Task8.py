'''Genrate all strong numbers within a user-specified range (e.g., 1 to 500) using functions.'''
import time as t
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
start_time = t.time()
def is_strong_number(num):
    original_num = num
    sum_of_factorials = 0
    while num > 0:
        digit = num % 10
        sum_of_factorials += factorial(digit)
        num //= 10
    return sum_of_factorials == original_num
def strong_numbers_in_range(start, end):
    strong_numbers = []
    for num in range(start, end + 1):
        if is_strong_number(num):
            strong_numbers.append(num)
    return strong_numbers
# Example usage
if __name__ == "__main__":
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))
    strong_numbers = strong_numbers_in_range(start_range, end_range)
    print(f"Strong numbers between {start_range} and {end_range}: {strong_numbers}")
end_time = t.time()
print(f"Time taken: {end_time - start_time} seconds")
# Analysis:
# Time Complexity: O(n * d) - where n is the number of numbers in the
# range and d is the number of digits in the largest number (for factorial calculation).
# Space Complexity: O(k) - where k is the number of strong numbers found in the
'''Generate an optimized version '''
print("\n")
print("Recreating an optimized version:")
def is_strong_number_optimized(num, factorial_cache={}):
    original_num = num
    sum_of_factorials = 0
    while num > 0:
        digit = num % 10
        if digit not in factorial_cache:
            factorial_cache[digit] = factorial(digit)
        sum_of_factorials += factorial_cache[digit]
        num //= 10
    return sum_of_factorials == original_num
start_time = t.time()
def strong_numbers_in_range_optimized(start, end):
    strong_numbers = []
    for num in range(start, end + 1):
        if is_strong_number_optimized(num):
            strong_numbers.append(num)
    return strong_numbers
# Example usage
if __name__ == "__main__":
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))
    strong_numbers = strong_numbers_in_range_optimized(start_range, end_range)
    print(f"Strong numbers between {start_range} and {end_range} (optimized): {strong_numbers}")
end_time = t.time()
print(f"Time taken (optimized): {end_time - start_time} seconds")
# Analysis:
# Time Complexity: O(n * d) - where n is the number of numbers in the
# range and d is the number of digits in the largest number (for factorial calculation).
