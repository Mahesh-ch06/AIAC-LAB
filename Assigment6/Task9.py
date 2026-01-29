'''create a function that parses a nested dictionary representing student information.
The function should extract and return:
Full Name
Branch
SGPA
Example Input:
{
    "student1": {
        "name": {"first": "Mahesh", "last": "Ch"},
        "branch": "CSE",
        "SGPA": 9.1
        },  
        "student2": {"name": {"first": "Rohan", "last": "Kumar"},
        "branch": "ECE",
        "SGPA": 8.7
        }'''
def extract_student_info(students_dict):
    extracted_info = []
    for student_key, student_data in students_dict.items():
        first_name = student_data['name']['first']
        last_name = student_data['name']['last']
        full_name = f"{first_name} {last_name}"
        branch = student_data['branch']
        sgpa = student_data['SGPA']
        extracted_info.append({
            'Full Name': full_name,
            'Branch': branch,
            'SGPA': sgpa
        })
    return extracted_info
# Example usage
if __name__ == "__main__":
    students = {
        "student1": {
            "name": {"first": "Mahesh", "last": "Ch"},
            "branch": "CSE",
            "SGPA": 9.1
        },
        "student2": {
            "name": {"first": "Rohan", "last": "Kumar"},
            "branch": "ECE",
            "SGPA": 8.7
        },
        "student3": {
            "name": {"first": "Anita", "last": "Sharma"},
            "branch": "ME",
            "SGPA": 8.9
        },
        "student4": {
            "name": {"first": "Priya", "last": "Singh"},
            "branch": "CE",
            "SGPA": 9.0
        },
        "student5": {
            "name": {"first": "Vikram", "last": "Patel"},
            "branch": "EE",
            "SGPA": 8.5
        }
    }
    student_info = extract_student_info(students)
    for info in student_info:
        print(info)
# Analysis:
# Time Complexity: O(n) - where n is the number of students in the dictionary.
# Space Complexity: O(n) - where n is the number of students, as we store the extracted information in a list.
