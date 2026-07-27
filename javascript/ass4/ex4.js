// Nested Object Manipulation
const company = {
  name: "ABC Ltd",
  address: {
    city: "Mumbai",
    state: "Maharashtra"
  },
  departments: {
    IT: 50,
    HR: 10,
    Finance: 15
  }
};
console.log("Company City:", company.address.city);
company.departments.Marketing = 20; 
console.log("After Adding Marketing:", company.departments);
company.departments.IT = 60; // updated from 50 to 60
console.log("After Updating IT:", company.departments);
const departmentNames = Object.keys(company.departments);
console.log("Department Names:", departmentNames);
