# Inventory Stock Alert
def analyze_inventory(products, stocks):
    print("Products with stock below 10:")
    for i in range(len(products)):
        if stocks[i] < 10:
            print(f"{products[i]} → {stocks[i]} units")
    total_stock = sum(stocks)
    print(f"\nTotal Inventory Count: {total_stock}")
    max_stock = max(stocks)
    max_index = stocks.index(max_stock)
    print(f"Product with Maximum Stock: {products[max_index]} ({max_stock} units)")
def main():
    products = []
    stocks = []
    n = int(input("Enter number of products: "))
    for i in range(n):
        name = input(f"Enter name of Product {i+1}: ")
        qty = int(input(f"Enter stock quantity of {name}: "))
        products.append(name)
        stocks.append(qty)
    analyze_inventory(products, stocks)
if __name__ == "__main__":
    main()
