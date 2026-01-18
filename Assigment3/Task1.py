# write a python code for palindrome number using functions

def is_palindrome(number):
    original_number = str(number)
    reversed_number = original_number[::-1]
    return original_number == reversed_number
num = int(input("Enter a number to check if it's a palindrome: "))
if is_palindrome(num):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")

