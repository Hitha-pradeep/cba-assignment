def add_product(cart, product, quantity):
    cart.append({"name": product, "quantity": quantity})
    print(f"{product} added with quantity {quantity}.")

def remove_product(cart, product):
    for item in cart:
        if item["name"].lower() == product.lower():
            cart.remove(item)
            print(f"{product} removed from cart.")
            return
    print(f"{product} not found in cart.")

def update_quantity(cart, product, quantity):
    for item in cart:
        if item["name"].lower() == product.lower():
            item["quantity"] = quantity
            print(f"{product} quantity updated to {quantity}.")
            return
    print(f"{product} not found in cart.")

def display_cart(cart):
    if not cart:
        print("Cart is empty.")
    else:
        print("Shopping Cart:")
        for item in cart:
            print(f"- {item['name']} (Quantity: {item['quantity']})")
def checkout(cart):
    cart.clear()
    print("Checkout complete. Cart is now empty.")
def main():
    cart = []
    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Product Quantity")
        print("4. Display Cart")
        print("5. Checkout")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            product = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            add_product(cart, product, quantity)
        elif choice == 2:
            product = input("Enter product name to remove: ")
            remove_product(cart, product)
        elif choice == 3:
            product = input("Enter product name to update: ")
            quantity = int(input("Enter new quantity: "))
            update_quantity(cart, product, quantity)
        elif choice == 4:
            display_cart(cart)
        elif choice == 5:
            checkout(cart)
        elif choice == 6:
            print("Exiting Shopping Cart System...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
