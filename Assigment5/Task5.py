def student_report(student_data):
    report = []
    for student, marks in student_data.items():
        average_score = sum(marks) / len(marks)
        status = "Pass" if average_score >= 40 else "Fail"
        report.append({
            "name": student,
            "average_score": average_score,
            "status": status
        })
    return report
# Example usage
if __name__ == "__main__":
    student_data = {
        "Alice": [85, 92, 78],
        "Bob": [58, 64, 70],
        "Charlie": [35, 40, 30]
    }
    summary_report = student_report(student_data)
    for student in summary_report:
        print(f"Name: {student['name']}, Average Score: {student['average_score']:.2f}, Status: {student['status']}")
# Analysis:
# Time Complexity: O(n) - where n is the number of students, as we iterate