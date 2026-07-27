# Online Shopping Cart
class ShoppingCart:
    def __init__(self, customer_name, product_name, quantity, price_per_item):
        self.customer_name = customer_name
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_item = price_per_item
    def calculate_total(self):
        return self.quantity * self.price_per_item
    def apply_discount(self):
        total = self.calculate_total()
        if total > 10000:
            discount = 0.20 * total
        elif total > 5000:
            discount = 0.10 * total
        else:
            discount = 0
        return total - discount
    def display_bill(self):
        total = self.calculate_total()
        final_amount = self.apply_discount()
        print(f"Customer Name: {self.customer_name}")
        print(f"Product: {self.product_name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price per Item: ₹{self.price_per_item}")
        print(f"Total Amount: ₹{total}")
        print(f"Final Bill after Discount: ₹{final_amount}")
cart1 = ShoppingCart("Alice", "Laptop", 1, 60000)
cart2 = ShoppingCart("Bob", "Phone", 2, 3000)
cart3 = ShoppingCart("Charlie", "Headphones", 1, 2000)
cart1.display_bill()
print("---------------")
cart2.display_bill()
print("---------------")
cart3.display_bill()
