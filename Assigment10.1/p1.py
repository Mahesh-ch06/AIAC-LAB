def area_of_rect(L,B):
    return L*B
print(area_of_rect(5,10))

#recfactored the above code with proper naming convention and added docstring for documentation
#add type hints for the function parameters and return type
def area_of_rectangle(length: float, breadth: float) -> float:
    """Calculate the area of a rectangle.

    Parameters:
        length (float): The length of the rectangle.
        breadth (float): The breadth of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * breadth
# Example usage:
length = 5.0
breadth = 10.0
area = area_of_rectangle(length, breadth)

#test the function with valid inputs
print(f"The area of the rectangle with length {length} and breadth {breadth} is: {area}")
