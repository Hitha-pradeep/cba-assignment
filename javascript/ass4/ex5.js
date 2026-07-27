// Shopping Cart System
const cart = [
  { name: "Phone", price: 20000, quantity: 1 },
  { name: "Headphones", price: 2000, quantity: 2 },
  { name: "Charger", price: 1000, quantity: 3 }
];

const totalValue = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);
console.log("Total Cart Value:", totalValue);

const updatedCart = cart.filter(item => item.name !== "Charger");
console.log("After Removing Charger:", updatedCart);

updatedCart.push({ name: "Tablet", price: 30000, quantity: 1 });
console.log("After Adding Tablet:", updatedCart);

const productNames = updatedCart.map(item => item.name);
console.log("Product Names:", productNames);
