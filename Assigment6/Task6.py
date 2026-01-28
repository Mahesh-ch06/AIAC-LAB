'''Write a function that finds all Armstrong numbers in a user-specified range (e.g., 1 to 1000).'''
def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == num
def armstrong_numbers_in_range(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    return armstrong_numbers
# Example usage
if __name__ == "__main__":
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))
    armstrong_numbers = armstrong_numbers_in_range(start_range, end_range)
    print(f"Armstrong numbers between {start_range} and {end_range}: {armstrong_numbers}")

print("\n")
print("Recreating using while loop:")
'''regenerate the using list comprehensions'''
def armstrong_numbers_in_range_list_comp(start, end):
    return [num for num in range(start, end + 1) if is_armstrong(num)]
# Example usage
if __name__ == "__main__":
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))
    armstrong_numbers = armstrong_numbers_in_range_list_comp(start_range, end_range)
    print(f"Armstrong numbers between {start_range} and {end_range} (using list comprehension): {armstrong_numbers}")
# Analysis:
# Time Complexity: O(n * d) - where n is the number of numbers in the range and d is the number of digits in the largest number. Each number requires checking each digit.
# Space Complexity: O(k) - where k is the number of Armstrong numbers found in the