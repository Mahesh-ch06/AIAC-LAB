'''read age from user to check voting eligibility
check if age is greater than or equal to 18
if yes print eligible to vote
otherwise print not eligible to vote
well commented code'''
age = int(input("Enter your age: "))  # Read age from user and convert to integer
# Check if the age is greater than or equal to 18
if age >= 18:
    print("Eligible to vote")  # Print if the user is eligible to vote
else:
    print("Not eligible to vote")  # Print if the user is not eligible to vote
