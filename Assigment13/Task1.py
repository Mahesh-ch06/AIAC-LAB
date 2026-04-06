'''# Legacy script with repeated logic
print("Area of Rectangle:", 5 * 10)
print("Perimeter of Rectangle:", 2 * (5 + 10))
print("Area of Rectangle:", 7 * 12)
print("Perimeter of Rectangle:", 2 * (7 + 12))
print("Area of Rectangle:", 10 * 15)
print("Perimeter of Rectangle:", 2 * (10 + 15))'''

# Refactored code using functions to eliminate repetition
def calculate_rectangle_area(length, width):
    return length * width
def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)
# Example usage:
rectangles = [(5, 10), (7, 12), (10, 15)]
for length, width in rectangles:
    area = calculate_rectangle_area(length, width)
    perimeter = calculate_rectangle_perimeter(length, width)
    print(f"Area of Rectangle: {area}")
    print(f"Perimeter of Rectangle: {perimeter}")
    