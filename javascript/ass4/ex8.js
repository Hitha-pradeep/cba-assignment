const orders = [
  {
    orderId: 101,
    customer: "John",
    items: ["Laptop", "Mouse"]
  },
  {
    orderId: 102,
    customer: "Emma",
    items: ["Phone", "Charger"]
  }
];
const johnOrder = orders.find(order => order.customer === "John");
if (johnOrder) {
  johnOrder.items.push("Keyboard");
}
console.log("After Adding Item to John's Order:", orders);
const phoneOrder = orders.find(order => order.items.includes("Phone"));
console.log("Customer who ordered Phone:", phoneOrder ? phoneOrder.customer : "Not found");
const allItems = orders.flatMap(order => order.items);
console.log("All Ordered Items:", allItems);
const totalItems = allItems.length;
console.log("Total Number of Items Ordered:", totalItems);
