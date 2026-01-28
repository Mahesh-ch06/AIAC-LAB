'''Genrate a all Happy Numbers within a user-specified range (e.g., 1 to 500) using functions.'''
import time as t
def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1
start_time = t.time()
def happy_numbers_in_range(start, end):
    happy_numbers = []
    for num in range(start, end + 1):
        if is_happy_number(num):
            happy_numbers.append(num)
    return happy_numbers
# Example usage
if __name__ == "__main__":
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))
    happy_numbers = happy_numbers_in_range(start_range, end_range)
    print(f"Happy numbers between {start_range} and {end_range}: {happy_numbers}")
end_time = t.time()
print(f"Time taken: {end_time - start_time} seconds")
# Analysis:
# Time Complexity: O(n * m) - where n is the number of numbers in the
# range and m is the average number of iterations to determine if a number is happy.
# Space Complexity: O(k) - where k is the number of happy numbers found in the
# range, as they are stored in a list.
print("\n")
print("Recreating an optimized version:")
'''regenerate an optimized version using a set to detect cycles instead of infinite loops'''
def is_happy_number_optimized(num):
    seen = set()
    while num != 1:
        if num in seen:
            return False
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return True
start_time = t.time()
def happy_numbers_in_range_optimized(start, end):
    happy_numbers = []
    for num in range(start, end + 1):
        if is_happy_number_optimized(num):
            happy_numbers.append(num)
    return happy_numbers
# Example usage
if __name__ == "__main__":
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))
    happy_numbers = happy_numbers_in_range_optimized(start_range, end_range)
    print(f"Happy numbers between {start_range} and {end_range} (optimized): {happy_numbers}")
end_time = t.time()
print(f"Time taken (optimized): {end_time - start_time} seconds")

# Analysis:
# Time Complexity: O(n * m) - where n is the number of numbers in the
# range and m is the average number of iterations to determine if a number is happy.
# Space Complexity: O(k) - where k is the number of happy numbers found in the
# range, as they are stored in a list.