# #write a one line code that checks if a number is positive or negative
# number = int(input("Enter a number: ")); print(f"{number} is positive." if number >= 0 else f"{number} is negative.")

# #write a well commented python code to check if a number is prime or not
# def is_prime(num):
#     """Check if a number is prime."""
#     if num <= 1:
#         return False  # Numbers less than or equal to 1 are not prime
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False  # Found a divisor, so it's not prime
#     return True  # No divisors found, so it's prime
# number = int(input("Enter a number: "))
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")



# '''
# read the number from user
# check it is divisible by 5 and 11
# if yes print print divisible by 5 and 11
# otherwise print not divisible by 5 and 11
# well commented code
# validate input to ensure it's an integer
# '''
# try:
#     number = int(input("Enter a number: "))  # Read input from user and convert to integer
#     # Check if the number is divisible by both 5 and 11
#     if number % 5 == 0 and number % 11 == 0:
#         print(f"{number} is divisible by both 5 and 11.")  # Print if divisible
#     else:
#         print(f"{number} is not divisible by both 5 and 11.")  # Print if not divisible
# except ValueError:
#     print("Invalid input! Please enter a valid integer.")  # Handle invalid input

'''
read the hall ticket number from user as a list take inputs 5 - 10 hall ticket numbers
check if hall ticket number is ends with 5 ,7 ,9
if give condition is true print valid hall ticket number
otherwise print invalid hall ticket number
well commented code
'''
hall_tickets = []  # Initialize an empty list to store hall ticket numbers
num_tickets = int(input("Enter the number of hall ticket numbers to input (5-10): "))
if 5 <= num_tickets <= 10:
    for _ in range(num_tickets):
        ticket = input("Enter hall ticket number: ")  # Read hall ticket number from user
        hall_tickets.append(ticket)  # Add the ticket number to the list

    for ticket in hall_tickets:
        # Check if the last digit of the hall ticket number is 5, 7, or 9
        if ticket[-1] in ['5', '7', '9']:
            print(f"{ticket} is a valid hall ticket number.")  # Print if valid
        else:
            print(f"{ticket} is an invalid hall ticket number.")  # Print if invalid
else:
    print("Please enter a number between 5 and 10.")  # Prompt if the number of tickets is out of range
    