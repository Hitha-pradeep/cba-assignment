function placeOrder(callback) {
  setTimeout(() => {
    console.log("Order Placed...");
    callback();
  }, 2000); // 2 seconds
}
function prepareFood(callback) {
  setTimeout(() => {
    console.log("Food is being prepared...");
    callback();
  }, 3000); // 3 seconds
}
function deliverFood(callback) {
  setTimeout(() => {
    console.log("Food is out for delivery...");
    callback();
  }, 2000); // 2 seconds
}
function foodDelivered() {
  console.log("Food Delivered Successfully!");
}
placeOrder(() => {
  prepareFood(() => {
    deliverFood(() => {
      foodDelivered();
    });
  });
});
