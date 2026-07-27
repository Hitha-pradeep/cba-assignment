def analyze_sales(sales):
    total_sales = sum(sales)
    max_sales = max(sales)
    max_month = sales.index(max_sales) + 1
    min_sales = min(sales)
    min_month = sales.index(min_sales) + 1
    above_50000 = []
    for i in range(len(sales)):
        if sales[i] > 50000:
            above_50000.append(i + 1)
    print("===================================")
    print(f"Monthly Sales: {sales}")
    print(f"Total Annual Sales : ₹{total_sales}")
    print(f"Maximum Sales      : ₹{max_sales} (Month {max_month})")
    print(f"Minimum Sales      : ₹{min_sales} (Month {min_month})")
    print(f"Months > ₹50,000   : {above_50000}")
    print("===================================")
def main():
    sales = []
    for i in range(12):
        val = float(input(f"Enter sales for Month {i+1}: "))
        sales.append(val)
    analyze_sales(sales)
if __name__ == "__main__":
    main()
