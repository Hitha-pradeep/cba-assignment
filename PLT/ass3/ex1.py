# Employee Attendance Tracker
class Employee:
    def __init__(self, emp_id, name, days_present):
        self.emp_id = emp_id
        self.name = name
        self.days_present = days_present
    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Days Present: {self.days_present}")
    def check_attendance(self):
        total_days = 5  # 5 working days in a week
        percentage = (self.days_present / total_days) * 100
        print(f"Attendance Percentage: {percentage:.2f}%")
        if percentage >= 90:
            print("Excellent Attendance")
        elif percentage >= 75:
            print("Good Attendance")
        else:
            print("Needs Improvement")
emp1 = Employee(101, "Alice", 5)
emp2 = Employee(102, "Bob", 4)
emp3 = Employee(103, "Charlie", 3)
emp1.display_details()
emp1.check_attendance()
print("---------------")
emp2.display_details()
emp2.check_attendance()
print("---------------")
emp3.display_details()
emp3.check_attendance()
