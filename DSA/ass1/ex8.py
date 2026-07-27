# Duplicate Customer ID Detector
def detect_duplicates(customer_ids):
    duplicates = []
    for cid in customer_ids:
        if customer_ids.count(cid) > 1 and cid not in duplicates:
            duplicates.append(cid)
    unique_ids = list(set(customer_ids))
    print("===================================")
    print(f"Customer IDs         : {customer_ids}")
    print(f"Duplicate IDs        : {duplicates}")
    print(f"Unique Customer IDs  : {unique_ids}")
    print("===================================")
def main():
    n = int(input("Enter number of customer IDs: "))
    customer_ids = []
    for i in range(n):
        cid = input(f"Enter Customer ID {i+1}: ")
        customer_ids.append(cid)
    detect_duplicates(customer_ids)
if __name__ == "__main__":
    main()
