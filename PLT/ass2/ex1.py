from abc import ABC, abstractmethod
# Base User class
class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.__password = password   # Encapsulation
    def login(self, email, password):
        return self.email == email and self.__password == password
# Customer inherits from User
class Customer(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.orders = []
    def place_order(self, order):
        self.orders.append(order)
# Restaurant class
class Restaurant:
    def __init__(self, restaurant_id, name):
        self.restaurant_id = restaurant_id
        self.name = name
        self.menu_items = []
    def add_menu_item(self, item):
        self.menu_items.append(item)
    def update_menu_item(self, item_id, new_price):
        for item in self.menu_items:
            if item.item_id == item_id:
                item.price = new_price
# MenuItem class
class MenuItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price
# Order class (Composition: contains MenuItems)
class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []
        self.status = "Placed"
        self.coupon = None
    def add_item(self, item):
        self.items.append(item)
    def apply_coupon(self, coupon_code):
        self.coupon = coupon_code
    def cancel_order(self):
        if self.status == "Placed":
            self.status = "Cancelled"
    def calculate_total(self):
        subtotal = sum(item.price for item in self.items)
        discount = 0
        if self.coupon == "SAVE10":
            discount = 0.1 * subtotal
        gst = 0.05 * subtotal
        delivery = 40
        return subtotal - discount + gst + delivery
# Abstract Payment class (Polymorphism)
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} via UPI.")
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} via Credit Card.")
class WalletPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} via Wallet.")
# Example Workflow
if __name__ == "__main__":
    # Create customer and restaurant
    customer = Customer(1, "Hitha", "hitha@example.com", "pass123")
    restaurant = Restaurant(101, "Food Palace")
    # Add menu items
    item1 = MenuItem(1, "Pizza", 250)
    item2 = MenuItem(2, "Burger", 150)
    restaurant.add_menu_item(item1)
    restaurant.add_menu_item(item2)
    # Place order
    order = Order(501, customer)
    order.add_item(item1)
    order.add_item(item2)
    order.apply_coupon("SAVE10")
    customer.place_order(order)
    # Generate bill
    total = order.calculate_total()
    print(f"Order Total: ₹{total}")
    # Make payment
    payment_method = UPIPayment()
    payment_method.pay(total)
    print(f"Order Status: {order.status}")
