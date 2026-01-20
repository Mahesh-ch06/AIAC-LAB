'''create a list of students with thier names give own names
from the list find the student name is palindrome or not
if yes print palindrome student name
otherwise print not palindrome student name
'''
def is_palindrome(name):
    # Check if the name is the same forwards and backwards
    return name == name[::-1]
students = ["Anna", "Bob", "Cathy", "David", "Eve"]  # List of student names
for student in students:
    if is_palindrome(student):
        print(f"{student} is a palindrome student name.")  # Print if the name is a palindrome
    else:
        print(f"{student} is not a palindrome student name.")  # Print if the name is not a palindrome