def add_student(students, student_id, name, course):
    students[student_id] = {"name": name, "course": course}
    print(f"Student {name} added successfully with ID {student_id}.")
def search_student(students, student_id):
    if student_id in students:
        print(f"Student ID: {student_id}, Name: {students[student_id]['name']}, Course: {students[student_id]['course']}")
    else:
        print(f"Student with ID {student_id} not found.")
def update_student(students, student_id, name=None, course=None):
    if student_id in students:
        if name:
            students[student_id]["name"] = name
        if course:
            students[student_id]["course"] = course
        print(f"Student ID {student_id} updated successfully.")
    else:
        print(f"Student with ID {student_id} not found.")
def delete_student(students, student_id):
    if student_id in students:
        del students[student_id]
        print(f"Student ID {student_id} deleted successfully.")
    else:
        print(f"Student with ID {student_id} not found.")
def display_students(students):
    if not students:
        print("No student records available.")
    else:
        print("Student Database:")
        for sid, details in students.items():
            print(f"ID: {sid}, Name: {details['name']}, Course: {details['course']}")
def main():
    students = {}
    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            sid = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            course = input("Enter Course: ")
            add_student(students, sid, name, course)
        elif choice == 2:
            sid = input("Enter Student ID to search: ")
            search_student(students, sid)
        elif choice == 3:
            sid = input("Enter Student ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            course = input("Enter new course (leave blank to skip): ")
            update_student(students, sid, name if name else None, course if course else None)
        elif choice == 4:
            sid = input("Enter Student ID to delete: ")
            delete_student(students, sid)
        elif choice == 5:
            display_students(students)
        elif choice == 6:
            print("Exiting Student Database...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
