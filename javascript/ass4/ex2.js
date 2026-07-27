// Product Inventory Management
const products = [
  { id: 1, name: "Laptop", stock: 10, price: 50000 },
  { id: 2, name: "Mouse", stock: 50, price: 500 },
  { id: 3, name: "Keyboard", stock: 30, price: 1500 }
];
products.push({ id: 4, name: "Monitor", stock: 15, price: 12000 });
console.log("After Adding:", products);
products.pop();
console.log("After Removing Last Product:", products);
const laptop = products.find(p => p.name === "Laptop");
if (laptop) {
  laptop.stock += 5;
}
console.log("After Increasing Laptop Stock:", products);
const lowStockProducts = products.filter(p => p.stock < 20);
console.log("Products with Stock < 20:", lowStockProducts);
