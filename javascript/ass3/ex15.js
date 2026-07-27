// Employee Salary Report
const employees = [
  { name: "Amit", salary: 30000 },
  { name: "Neha", salary: 45000 },
  { name: "Raj", salary: 28000 },
  { name: "Priya", salary: 50000 }
];

console.log("Employee Names:");
for (const emp of employees) {
  console.log(emp.name);
}

const updatedSalaries = employees.map(emp => emp.salary * 1.1);
function getHighestSalary(arr) {
  return Math.max(...arr);
}
console.log("\nUpdated Salaries:", updatedSalaries);
console.log("Highest Salary:", getHighestSalary(updatedSalaries));
