class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, designation, basic_salary, experience):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.designation = designation
        self.basic_salary = basic_salary
        self.experience = experience

    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Designation: {self.designation}")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"Experience: {self.experience} years")

    def calculate_allowance(self):
        if self.experience > 10:
            allowance = 0.20 * self.basic_salary
        elif 5 <= self.experience <= 10:
            allowance = 0.10 * self.basic_salary
        else:
            allowance = 0.05 * self.basic_salary
        return allowance
# Creating an instance of Employee
employee = Employee(emp_id=101, emp_name="John Doe", emp_salary=75000
                    , designation="Software Engineer", basic_salary=60000, experience=8)
employee1 = Employee(emp_id=102, emp_name="Jane Smith", emp_salary=85000
                    , designation="Senior Developer", basic_salary=70000, experience=12)
employee2 = Employee(emp_id=103, emp_name="Alice Johnson", emp_salary=50000
                    , designation="Junior Developer", basic_salary=40000, experience=3)
employee3 = Employee(emp_id=104, emp_name="Bob Brown", emp_salary=95000
                    , designation="Team Lead", basic_salary=80000, experience=15)
# Displaying employee details
employee.display_details()
# Calculating and printing allowance
allowance = employee.calculate_allowance()
print(f"Calculated Allowance: {allowance}")
print("\n")
employee1.display_details()
allowance1 = employee1.calculate_allowance()
print(f"Calculated Allowance: {allowance1}")
print("\n")
employee2.display_details()
allowance2 = employee2.calculate_allowance()
print(f"Calculated Allowance: {allowance2}")
print("\n")
employee3.display_details()
allowance3 = employee3.calculate_allowance()
print(f"Calculated Allowance: {allowance3}")
# Analysis:
# Time Complexity: O(1) - The operations in the methods are constant time operations.
# Space Complexity: O(1) - The space used by the instance variables is constant.
# Compare this snippet from Assigment6/Task10.py:
