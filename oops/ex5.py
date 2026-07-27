# Student Examination Result System
class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks 
    def calculate_total(self):
        return sum(self.marks)
    def calculate_percentage(self):
        return self.calculate_total() / len(self.marks)
    def assign_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return "A"
        elif percentage >= 80:
            return "B"
        elif percentage >= 70:
            return "C"
        elif percentage >= 60:
            return "D"
        else:
            return "F"
    def display_report(self):
        print("===================================")
        print(f"Roll Number : {self.roll_number}")
        print(f"Name        : {self.name}")
        print(f"Marks       : {self.marks}")
        print(f"Total Marks : {self.calculate_total()}")
        print(f"Percentage  : {self.calculate_percentage():.2f}%")
        print(f"Grade       : {self.assign_grade()}")
        print("===================================")
def main():
    n = int(input("Enter number of students: "))
    students = []
    for i in range(n):
        print(f"\nEnter details for Student {i+1}:")
        roll_number = input("Roll Number: ")
        name = input("Name: ")
        marks = []
        for j in range(5):
            mark = int(input(f"Enter marks for Subject {j+1}: "))
            marks.append(mark)
        student = Student(roll_number, name, marks)
        students.append(student)
    for student in students:
        student.display_report()
if __name__ == "__main__":
    main()
