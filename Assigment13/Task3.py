'''marks = 85
if marks >= 90:
print("Grade A")
elif marks >= 75:
print("Grade B")
else:
print("Grade C")
marks = 72
if marks >= 90:
print("Grade A")
elif marks >= 75:
print("Grade B")
else:
print("Grade C")

refactore the abobe code using function to eliminate repetition'''
def calculate_grade(marks):
    if marks >= 90:
        return "Grade A"
    elif marks >= 75:
        return "Grade B"
    else:
        return "Grade C"
# Example usage:
marks_list = [85, 72]
for marks in marks_list:
    grade = calculate_grade(marks)
    print(f"Marks: {marks} - {grade}")
    