const orders = [
  {
    id: 1,
    customer: "John",
    products: [
      { name: "Laptop", price: 50000 },
      { name: "Mouse", price: 500 }
    ]
  },
  {
    id: 2,
    customer: "Emma",
    products: [
      { name: "Phone", price: 30000 },
      { name: "Headphones", price: 2000 }
    ]
  }
];
orders.forEach(order => {
  const total = order.products.reduce((sum, product) => sum + product.price, 0);
  order.totalSpent = total;
});
console.log("Orders with Total Spent:", orders);
const topCustomer = orders.reduce((prev, curr) =>
  curr.totalSpent > prev.totalSpent ? curr : prev
);
console.log("Customer Who Spent the Most:", topCustomer.customer);
const allProductNames = orders.flatMap(order => order.products.map(p => p.name));
console.log("All Product Names:", allProductNames);
const totalProducts = allProductNames.length;
console.log("Total Number of Products Sold:", totalProducts);
const expensiveProducts = orders.flatMap(order =>
  order.products.filter(p => p.price > 10000)
);
console.log("Products Costing More Than ₹10,000:", expensiveProducts);
