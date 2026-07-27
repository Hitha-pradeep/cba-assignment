# Shopping Cart Manager
def add_product(cart, price):
    cart.append(price)
    print(f"Added product with price ₹{price}")

def remove_product(cart, price):
    if price in cart:
        cart.remove(price)
        print(f"Removed product with price ₹{price}")
    else:
        print("Product price not found in cart!")

def display_cart_value(cart):
    total = sum(cart)
    print(f"Total Cart Value: ₹{total}")

def find_most_expensive(cart):
    if cart:
        print(f"Most Expensive Product: ₹{max(cart)}")
    else:
        print("Cart is empty!")
def main():
    cart = []
    while True:
        print("\n===== Shopping Cart Menu =====")
        print("1. Add Product Price")
        print("2. Remove Product Price")
        print("3. Display Total Cart Value")
        print("4. Find Most Expensive Product")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            price = float(input("Enter product price: "))
            add_product(cart, price)
        elif choice == 2:
            price = float(input("Enter product price to remove: "))
            remove_product(cart, price)
        elif choice == 3:
            display_cart_value(cart)
        elif choice == 4:
            find_most_expensive(cart)
        elif choice == 5:
            print("Exiting Shopping Cart Manager...")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()
