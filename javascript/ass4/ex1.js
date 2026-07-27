// Employee Salary Analysis
const employees = [
  { id: 1, name: "John", salary: 50000, department: "IT" },
  { id: 2, name: "Emma", salary: 70000, department: "HR" },
  { id: 3, name: "David", salary: 60000, department: "IT" },
  { id: 4, name: "Sophia", salary: 80000, department: "Finance" }
];
const itEmployees = employees.filter(emp => emp.department === "IT");
console.log("IT Employees:", itEmployees);

const totalSalary = employees.reduce((sum, emp) => sum + emp.salary, 0);
console.log("Total Salary:", totalSalary);

const highestSalaryEmployee = employees.reduce((prev, curr) => 
  (curr.salary > prev.salary ? curr : prev)
);
console.log("Highest Salary Employee:", highestSalaryEmployee);

const employeeNames = employees.map(emp => emp.name);
console.log("Employee Names:", employeeNames);
