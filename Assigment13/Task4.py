'''num = int(input("Enter number: "))
square = num * num
print("Square:", square)
refactor the above code using a function to eliminate repetition'''
def calculate_square(num):
    return num * num
# Example usage:
numbers = [int(input("Enter number: "))]
for num in numbers:
    square = calculate_square(num)
    print(f"Square: {square}")
    
