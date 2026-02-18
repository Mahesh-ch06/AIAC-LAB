'''Generate a python code that checks whether a number is a magic number or not. give me an analysis of time and space complexity. give me optimized code

examples
Input: 123
Output: Not a Magic Number
Input: 19
Output: Magic Number
Input: 18
Output: Not a Magic Number
Input: 0
Output: Magic Number
'''
def is_magic_number(num):
    if num == 0:
        return True
    
    sum_of_digits = 0
    while num > 0:
        digit = num % 10
        sum_of_digits += digit
        num //= 10
    
    return sum_of_digits == 1
# Example usage
if __name__ == "__main__":
    numbers = [123, 19, 18, 0]
    for number in numbers:
        if is_magic_number(number):
            print(f"{number} is a Magic Number")
        else:
            print(f"{number} is Not a Magic Number")
# Analysis:
# Time Complexity: O(d) where d is the number of digits in the input number.
# Space Complexity: O(1) - The space used does not grow with input size; it uses a fixed amount of space.
# Optimized Code
def is_magic_number(num):
    if num == 0:
        return True
    
    sum_of_digits = sum(int(digit) for digit in str(num))
    
    return sum_of_digits == 1
# Example usage
if __name__ == "__main__":
    numbers = [123, 19, 18, 0]
    for number in numbers:
        if is_magic_number(number):
            print(f"{number} is a Magic Number")
        else:
            print(f"{number} is Not a Magic Number")
# Analysis:
# Time Complexity: O(d) where d is the number of digits in the input number,
# Space Complexity: O(1) - The space used does not grow with input size; it uses a fixed amount of space.
'''generate a python code for factorial of number using recursion.. give me an analysis of time and space complexity. give me optimized code'''