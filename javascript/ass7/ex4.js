function orderPlaced() {
  return new Promise((resolve) => {
    resolve("Order Placed");
  });
}

function paymentSuccessful(success = true) {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve("Payment Successful");
    } else {
      reject("Payment Failed");
    }
  });
}

function productShipped() {
  return new Promise((resolve) => {
    resolve("Product Shipped");
  });
}

// Execution with Promise chaining
orderPlaced()
  .then((msg) => {
    console.log(msg);
    return paymentSuccessful(true); // change to false to simulate failure
  })
  .then((msg) => {
    console.log(msg);
    return productShipped();
  })
  .then((msg) => {
    console.log(msg);
    console.log("Order Completed");
  })
  .catch((error) => {
    console.log(error);
  });
