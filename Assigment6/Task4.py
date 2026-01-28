'''Create a class Teacher with attributes teacher_id, name, subject, and experience. Add a method to display teacher details.'''
class Teacher:
    def __init__(self, teacher_id, name, subject, experience):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject
        self.experience = experience

    def display_details(self):
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")
        print(f"Experience: {self.experience} years")
# Example usage
if __name__ == "__main__":
    teacher1 = Teacher(101, "Alice Johnson", "Mathematics", 10)
    teacher2 = Teacher(102, "Bob Smith", "Science", 8)

    print("Teacher 1 Details:")
    teacher1.display_details()
    print("\nTeacher 2 Details:")
    teacher2.display_details()