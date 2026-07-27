function atmWithdrawal(balance) {
  return new Promise((resolve, reject) => {
    if (balance >= 5000) {
      resolve("Withdrawal Successful");
    } else {
      reject("Insufficient Balance");
    }
  });
}

// Example usage:
let accountBalance = 6000; // Try changing this to 4000 for failure case

atmWithdrawal(accountBalance)
  .then((message) => {
    console.log(message);
  })
  .catch((error) => {
    console.log(error);
  });
