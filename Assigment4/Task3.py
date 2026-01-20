'''create a grading system 
example
A - 95
B - 85
C - 75
D - 60
F - below 60
'''
def grade_system(score):
    if score >= 95:
        return 'A'
    elif score >= 85:
        return 'B'
    elif score >= 75:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
# Example usage
input_score = 88
result = grade_system(input_score)
print(result)  # Output: B
# Example usage
input_score2 = 72
result2 = grade_system(input_score2)
print(result2)  # Output: C
# Example usage
input_score3 = 59
result3 = grade_system(input_score3)
print(result3)  # Output: F