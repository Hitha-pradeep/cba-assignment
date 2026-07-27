# Sales Performance Comparison
def compare_sales(sales1, sales2):
    print("\n===== Month-wise Comparison =====")
    for i in range(len(sales1)):
        if sales1[i] > sales2[i]:
            print(f"Month {i+1}: Salesperson 1 performed better ({sales1[i]} vs {sales2[i]})")
        elif sales2[i] > sales1[i]:
            print(f"Month {i+1}: Salesperson 2 performed better ({sales2[i]} vs {sales1[i]})")
        else:
            print(f"Month {i+1}: Both performed equally ({sales1[i]})")
    total1 = sum(sales1)
    total2 = sum(sales2)
    print("\n=====Annual Sales =====")
    print(f"Salesperson 1: ₹{total1}")
    print(f"Salesperson 2: ₹{total2}")
def main():
    sales1 = []
    sales2 = []
    print("Enter monthly sales for Salesperson 1:")
    for i in range(12):
        val = float(input(f"Month {i+1}: "))
        sales1.append(val)
    print("\nEnter monthly sales for Salesperson 2:")
    for i in range(12):
        val = float(input(f"Month {i+1}: "))
        sales2.append(val)
    compare_sales(sales1, sales2)
if __name__ == "__main__":
    main()
