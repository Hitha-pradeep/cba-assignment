# Food Delivery Order System
class Order:
    def __init__(self, customer_name, food_item, quantity, price):
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price
    def calculate_total(self):
        return self.quantity * self.price
    def final_bill(self):
        total = self.calculate_total()
        if total > 800:
            print("Eligible for Free Delivery")
            return total
        else:
            print("Delivery Charge Applied")
            return total + 60
    def display_bill(self):
        total = self.calculate_total()
        final_amount = self.final_bill()
        print(f"Customer Name: {self.customer_name}")
        print(f"Food Item: {self.food_item}")
        print(f"Quantity: {self.quantity}")
        print(f"Price per Item: ₹{self.price}")
        print(f"Total Amount: ₹{total}")
        print(f"Final Bill: ₹{final_amount}")
        print("---------------")
order1 = Order("Alice", "Pizza", 2, 500)
order2 = Order("Bob", "Burger", 3, 200)
order3 = Order("Charlie", "Pasta", 1, 900)
order1.display_bill()
order2.display_bill()
order3.display_bill()
