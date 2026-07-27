def add_employee(employees, name):
    employees.append(name)
    print(f"{name} added successfully.")

def remove_employee(employees, name):
    if name in employees:
        employees.remove(name)
        print(f"{name} removed successfully.")
    else:
        print(f"{name} not found in the directory.")

def search_employee(employees, name):
    if name in employees:
        print(f"{name} is present in the directory.")
    else:
        print(f"{name} not found.")

def display_employees(employees):
    print("Employee List:")
    for emp in employees:
        print(emp)

def count_employees(employees):
    print(f"Total Employees: {len(employees)}")

def main():
    employees = []
    while True:
        print("\n--- Employee Directory Menu ---")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Search Employee")
        print("4. Display All Employees")
        print("5. Count Employees")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter employee name to add: ")
            add_employee(employees, name)
        elif choice == 2:
            name = input("Enter employee name to remove: ")
            remove_employee(employees, name)
        elif choice == 3:
            name = input("Enter employee name to search: ")
            search_employee(employees, name)
        elif choice == 4:
            display_employees(employees)
        elif choice == 5:
            count_employees(employees)
        elif choice == 6:
            print("Exiting Employee Directory...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
