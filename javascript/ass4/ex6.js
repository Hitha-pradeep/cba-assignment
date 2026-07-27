// Dynamic Object Properties
const user = {
  name: "Rahul",
  age: 25
};
user["email"] = "rahul@example.com";
console.log("After Adding Email:", user);
delete user.age;
console.log("After Deleting Age:", user);
console.log("All Keys:", Object.keys(user));
console.log("All Values:", Object.values(user));
console.log("Does email exist?", user.hasOwnProperty("email"));
