# Online Shopping Cart System
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    def item_total(self):
        return self.price * self.quantity
class ShoppingCart:
    def __init__(self):
        self.products = []  
    def add_product(self, product):
        self.products.append(product)
    def calculate_grand_total(self):
        return sum(product.item_total() for product in self.products)
    def apply_discount(self, total):
        if total > 5000:
            return total * 0.85 
        elif total > 3000:
            return total * 0.90  
        else:
            return total
    def print_invoice(self):
        print("\n========== Final Invoice ==========")
        for product in self.products:
            print(f"Product ID: {product.product_id}")
            print(f"Name      : {product.name}")
            print(f"Price     : ₹{product.price}")
            print(f"Quantity  : {product.quantity}")
            print(f"Item Total: ₹{product.item_total()}")
            print("-----------------------------------")
        grand_total = self.calculate_grand_total()
        final_amount = self.apply_discount(grand_total)
        print(f"Grand Total (Before Discount): ₹{grand_total}")
        print(f"Final Amount (After Discount): ₹{final_amount}")
        print("===================================")
def main():
    cart = ShoppingCart()
    n = int(input("Enter number of products to add: "))
    for i in range(n):
        print(f"\nEnter details for Product {i+1}:")
        product_id = input("Product ID: ")
        name = input("Product Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        product = Product(product_id, name, price, quantity)
        cart.add_product(product)
    cart.print_invoice()
if __name__ == "__main__":
    main()
