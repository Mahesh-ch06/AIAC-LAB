'''create a filter out the indian mobile numbers from the given text file the condition is that the number should start with 6,7,8 or 9 and it should be of 10 digit long  create some set of examples'''
import re
def filter_indian_mobile_numbers(file_path):
    indian_mobile_numbers = []
    pattern = re.compile(r'\b[6-9]\d{9}\b')

    with open(file_path, 'r') as file:
        content = file.read()
        matches = pattern.findall(content)
        indian_mobile_numbers.extend(matches)

    return indian_mobile_numbers
# Example usage
if __name__ == "__main__":
    file_path = 'mobile_numbers.txt'  # Replace with your file path
    filtered_numbers = filter_indian_mobile_numbers(file_path)
    print("Filtered Indian Mobile Numbers:")
    for number in filtered_numbers:
        print(number)
