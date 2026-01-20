'''read marks from students
check if marks is greater than or equal to 40
if yes print pass
otherwise print fail
well commented code'''
marks = float(input("Enter the marks obtained by the student: "))  # Read marks from user and convert to float
# Check if the marks are greater than or equal to 40
if marks >= 40:
    print("Pass")  # Print "Pass" if marks are 40 or more
else:
    print("Fail")  # Print "Fail" if marks are less than 40
    