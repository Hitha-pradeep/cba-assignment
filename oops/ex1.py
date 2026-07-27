# Employee Attendance Management System
class Employee:
    def __init__(self, emp_id, name, department, working_days, days_present):
        self.__emp_id = emp_id
        self.__name = name
        self.__department = department
        self.__working_days = working_days
        self.__days_present = days_present
    def calculate_attendance(self):
        return (self.__days_present / self.__working_days) * 100
    def attendance_status(self):
        percentage = self.calculate_attendance()
        if percentage >= 90:
            return "Excellent"
        elif percentage >= 75:
            return "Good"
        else:
            return "Needs Improvement"
    def display_report(self):
        print("===================================")
        print(f"Employee ID     : {self.__emp_id}")
        print(f"Name            : {self.__name}")
        print(f"Department      : {self.__department}")
        print(f"Working Days    : {self.__working_days}")
        print(f"Days Present    : {self.__days_present}")
        print(f"Attendance %    : {self.calculate_attendance():.2f}%")
        print(f"Status          : {self.attendance_status()}")
        print("===================================")
def main():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    working_days = int(input("Enter total working days in month: "))
    days_present = int(input("Enter number of days present: "))
    emp = Employee(emp_id, name, department, working_days, days_present)
    emp.display_report()
if __name__ == "__main__":
    main()
