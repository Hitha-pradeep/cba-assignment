# Electricity Bill Calculator
class ElectricityBill:
    def __init__(self, consumer_no, customer_name, units_consumed):
        self.consumer_no = consumer_no
        self.customer_name = customer_name
        self.units_consumed = units_consumed
    def calculate_bill(self):
        units = self.units_consumed
        amount = 0
        if units <= 100:
            amount = units * 5
        else:
            if units <= 200:
                amount = (100 * 5) + ((units - 100) * 7)
            else:
                amount = (100 * 5) + (100 * 7) + ((units - 200) * 10)
        surcharge = 0
        if amount > 5000:
            surcharge = 0.05 * amount
            final_amount = amount + surcharge
        else:
            final_amount = amount
        return amount, surcharge, final_amount
    def display_bill(self):
        amount, surcharge, final_amount = self.calculate_bill()
        print(f"Consumer Number: {self.consumer_no}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Units Consumed: {self.units_consumed}")
        print(f"Total Amount: ₹{amount}")
        print(f"Surcharge: ₹{surcharge}")
        print(f"Final Bill: ₹{final_amount}")
        print("---------------")
bill1 = ElectricityBill(101, "Alice", 95)
bill2 = ElectricityBill(102, "Bob", 150)
bill3 = ElectricityBill(103, "Charlie", 350)
bill1.display_bill()
bill2.display_bill()
bill3.display_bill()
