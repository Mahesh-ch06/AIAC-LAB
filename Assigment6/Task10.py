'''Genrate a perfect numbers within a user-specified range (e.g., 1 to 1000) using functions.'''
import time as t
def is_perfect_number(num):
    if num < 2:
        return False
    sum_of_divisors = 1  # 1 is a proper divisor
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
    return sum_of_divisors == num
start_time = t.time()
def perfect_numbers_in_range(start, end):
    perfect_numbers = []
    for num in range(start, end + 1):
        if is_perfect_number(num):
            perfect_numbers.append(num)
    return perfect_numbers
# Example usage
if __name__ == "__main__":
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))
    perfect_numbers = perfect_numbers_in_range(start_range, end_range)
    print(f"Perfect numbers between {start_range} and {end_range}: {perfect_numbers}")
end_time = t.time()
print(f"Time taken: {end_time - start_time} seconds")
# Analysis:
# Time Complexity: O(n * √m) - where n is the number of numbers in the
# range and m is the average number to check for perfectness.
# Space Complexity: O(k) - where k is the number of perfect numbers found in the
# range, as they are stored in a list.
'''Generate an optimized version using divisor check only up to √n'''
print("\n")
print("Recreating an optimized version:")
def is_perfect_number_optimized(num):
    if num < 2:
        return False
    sum_of_divisors = 1  # 1 is a proper divisor
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
    return sum_of_divisors == num
start_time = t.time()
def perfect_numbers_in_range_optimized(start, end):
    perfect_numbers = []
    for num in range(start, end + 1):
        if is_perfect_number_optimized(num):
            perfect_numbers.append(num)
    return perfect_numbers
# Example usage
if __name__ == "__main__":
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))
    perfect_numbers = perfect_numbers_in_range_optimized(start_range, end_range)
    print(f"Perfect numbers between {start_range} and {end_range} (optimized): {perfect_numbers}")
end_time = t.time()
print(f"Time taken (optimized): {end_time - start_time} seconds")
# Analysis:
# Time Complexity: O(n * √m) - where n is the number of numbers in
# the range and m is the average number to check for perfectness.
# Space Complexity: O(k) - where k is the number of perfect numbers found in the
# range, as they are stored in a list.

