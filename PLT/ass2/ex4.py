from abc import ABC, abstractmethod
# ---------------- Employee ----------------
class Employee(ABC):
    def __init__(self, emp_id, name):
        self.__emp_id = emp_id
        self.__name = name

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__emp_id

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def calculate_tax(self):
        pass

    def generate_salary_slip(self):
        salary = self.calculate_salary()
        tax = self.calculate_tax()
        net_salary = salary - tax

        print("\n------ Salary Slip ------")
        print("Employee ID :", self.get_id())
        print("Employee Name :", self.get_name())
        print("Gross Salary : ₹", salary)
        print("Tax : ₹", tax)
        print("Net Salary : ₹", net_salary)
        print("-------------------------")

# ---------------- Full Time Employee ----------------
class FullTimeEmployee(Employee):
    BONUS = 5000

    def __init__(self, emp_id, name, basic_salary):
        super().__init__(emp_id, name)
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary + FullTimeEmployee.BONUS

    def calculate_tax(self):
        salary = self.calculate_salary()

        if salary > 100000:
            return salary * 0.20
        elif salary > 50000:
            return salary * 0.10
        else:
            return salary * 0.05

# ---------------- Part Time Employee ----------------
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hours, rate, overtime_hours):
        super().__init__(emp_id, name)
        self.hours = hours
        self.rate = rate
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        overtime = self.overtime_hours * self.rate * 1.5
        return (self.hours * self.rate) + overtime

    def calculate_tax(self):
        salary = self.calculate_salary()

        if salary > 50000:
            return salary * 0.10
        else:
            return salary * 0.05

# ---------------- Intern ----------------
class Intern(Employee):
    def __init__(self, emp_id, name, stipend):
        super().__init__(emp_id, name)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend

    def calculate_tax(self):
        return 0

# ---------------- Payroll ----------------
class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(employee.get_name(), "added successfully.")

    def generate_payroll(self):
        print("\n========= PAYROLL =========")
        for emp in self.employees:
            emp.generate_salary_slip()

# ---------------- Main ----------------
payroll = Payroll()

# Add Employees
emp1 = FullTimeEmployee(101, "Alice", 60000)
emp2 = PartTimeEmployee(102, "Bob", 120, 300, 10)
emp3 = Intern(103, "Charlie", 15000)

payroll.add_employee(emp1)
payroll.add_employee(emp2)
payroll.add_employee(emp3)

# Generate Payroll
payroll.generate_payroll()