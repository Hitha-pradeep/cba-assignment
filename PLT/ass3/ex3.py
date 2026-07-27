# Student Grade Management
class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks  
    def calculate_total(self):
        return sum(self.marks)
    def calculate_average(self):
        return self.calculate_total() / len(self.marks)
    def assign_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"
    def display_report(self):
        print(f"Roll Number: {self.roll_number}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Total: {self.calculate_total()}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Grade: {self.assign_grade()}")
        print("---------------")
students = [
    Student(101, "Alice", [95, 92, 88, 90, 96]),
    Student(102, "Bob", [70, 65, 68, 72, 74]),
    Student(103, "Charlie", [40, 45, 50, 42, 38]),
    Student(104, "David", [30, 25, 35, 28, 32])
]
for student in students:
    student.display_report()
