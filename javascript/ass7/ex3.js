function checkResult(marks) {
  return new Promise((resolve, reject) => {
    if (marks >= 35) {
      resolve("Student Passed");
    } else {
      reject("Student Failed");
    }
  });
}

// Example usage
let marks = 80; // Try changing this to 25 for failure case

checkResult(marks)
  .then((message) => {
    console.log(message);
  })
  .catch((error) => {
    console.log(error);
  });
