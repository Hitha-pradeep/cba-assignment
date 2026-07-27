# Employee Salary Processing
def process_salaries(salaries):
    updated_salaries = [sal * 1.10 for sal in salaries]
    print("Updated Salaries:", updated_salaries)
    print("Employees earning above ₹50,000:")
    for sal in updated_salaries:
        if sal > 50000:
            print(f"₹{sal:.2f}")
    return updated_salaries
def main():
    n = int(input("Enter number of employees: "))
    salaries = []
    for i in range(n):
        sal = float(input(f"Enter salary of Employee {i+1}: "))
        salaries.append(sal)
    process_salaries(salaries)
if __name__ == "__main__":
    main()
