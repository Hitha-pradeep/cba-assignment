# Inventory Management System
class Product:
    def __init__(self, product_id, name, quantity_available, min_stock_level):
        self.product_id = product_id
        self.name = name
        self.quantity_available = quantity_available
        self.min_stock_level = min_stock_level
    def sell_product(self, qty):
        if qty <= 0:
            print("Invalid quantity! Enter a positive number.")
        elif qty > self.quantity_available:
            print("Error: Cannot sell more than available stock.")
        else:
            self.quantity_available -= qty
            print(f"{qty} units of '{self.name}' sold successfully.")
    def restock_product(self, qty):
        if qty <= 0:
            print("Invalid quantity! Enter a positive number.")
        else:
            self.quantity_available += qty
            print(f"{qty} units of '{self.name}' restocked successfully.")
    def check_stock_status(self):
        if self.quantity_available == 0:
            return "Out of Stock"
        elif self.quantity_available <= self.min_stock_level:
            return "Low Stock"
        else:
            return "Stock Available"
    def display_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.name}")
        print(f"Quantity Available: {self.quantity_available}")
        print(f"Stock Status: {self.check_stock_status()}")
        print("---------------")
product = Product(101, "Laptop", 10, 3)
while True:
    print("\n--- Inventory Menu ---")
    print("1. Sell Product")
    print("2. Restock Product")
    print("3. Check Stock Status")
    print("4. Display Product Details")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
    if choice == 1:
        try:
            qty = int(input("Enter quantity to sell: "))
            product.sell_product(qty)
        except ValueError:
            print("Invalid input! Please enter a number.")
    elif choice == 2:
        try:
            qty = int(input("Enter quantity to restock: "))
            product.restock_product(qty)
        except ValueError:
            print("Invalid input! Please enter a number.")
    elif choice == 3:
        print("Stock Status:", product.check_stock_status())
    elif choice == 4:
        product.display_details()
    elif choice == 5:
        print("Exiting Inventory System. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
