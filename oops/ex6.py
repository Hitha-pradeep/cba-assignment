# Vehicle Rental System
class Vehicle:
    def __init__(self, vehicle_id, name, vtype, price_per_day):
        self.__vehicle_id = vehicle_id
        self.__name = name
        self.__vtype = vtype
        self.__price_per_day = price_per_day
    def calculate_rent(self, days):
        total = self.__price_per_day * days
        if days > 10:
            total *= 0.80   
        elif days > 5:
            total *= 0.90  
        return total
    def display_bill(self, days):
        print("===================================")
        print(f"Vehicle ID       : {self.__vehicle_id}")
        print(f"Vehicle Name     : {self.__name}")
        print(f"Vehicle Type     : {self.__vtype}")
        print(f"Rental Price/Day : ₹{self.__price_per_day}")
        print(f"Rental Days      : {days}")
        print(f"Final Bill       : ₹{self.calculate_rent(days)}")
        print("===================================")
def main():
    car = Vehicle("C101", "Honda City", "Car", 1500)
    bike = Vehicle("B201", "Royal Enfield", "Bike", 500)
    print("Choose Vehicle: 1. Car  2. Bike")
    choice = int(input("Enter choice (1/2): "))
    days = int(input("Enter number of rental days: "))
    if choice == 1:
        car.display_bill(days)
    elif choice == 2:
        bike.display_bill(days)
    else:
        print("Invalid Choice!")
if __name__ == "__main__":
    main()
