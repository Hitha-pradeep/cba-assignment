# Online Exam Attendance
def analyze_attendance(attendance_list):
    present_count = attendance_list.count("P")
    absent_count = attendance_list.count("A")
    total_students = len(attendance_list)
    attendance_percentage = (present_count / total_students) * 100
    print("===================================")
    print(f"Attendance List       : {attendance_list}")
    print(f"Present Students      : {present_count}")
    print(f"Absent Students       : {absent_count}")
    print(f"Attendance Percentage : {attendance_percentage:.2f}%")
    print("===================================")
def main():
    attendance_list = []
    n = int(input("Enter number of students: "))
    for i in range(n):
        status = input(f"Enter attendance for Student {i+1} (P/A): ").upper()
        attendance_list.append(status)
    analyze_attendance(attendance_list)
if __name__ == "__main__":
    main()
