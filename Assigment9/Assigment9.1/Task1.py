# write a function for documentation using Docstring that finds the maximum number in a list of numbers.
def find_max(numbers):
    """
    Finds the maximum number in a list of numbers.
    
    Parameters:
        numbers (list): A list of numbers.
        
    Returns:
        int/float: The maximum number in the list.
        
    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("The list is empty.")
    
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num
# Example usage:
numbers = [3, 5, 7, 2, 8]
max_number = find_max(numbers)
print(f"The maximum number in the list is: {max_number}")
