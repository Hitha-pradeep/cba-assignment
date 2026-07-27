# Bus Seat Reservation System
class Bus:
    def __init__(self, total_seats=20):
        self.seats = [0] * total_seats
    def count_available(self):
        return self.seats.count(0)
    def book_seat(self, seat_no):
        if 1 <= seat_no <= len(self.seats):
            if self.seats[seat_no - 1] == 0:
                self.seats[seat_no - 1] = 1
                print(f"Seat {seat_no} booked successfully.")
            else:
                print(f"Seat {seat_no} is already booked.")
        else:
            print("Invalid seat number!")
    def cancel_booking(self, seat_no):
        if 1 <= seat_no <= len(self.seats):
            if self.seats[seat_no - 1] == 1:
                self.seats[seat_no - 1] = 0
                print(f"Seat {seat_no} booking cancelled.")
            else:
                print(f"Seat {seat_no} is not booked.")
        else:
            print("Invalid seat number!")
    def display_seats(self):
        print("\n===== Seat Status =====")
        for i, status in enumerate(self.seats, start=1):
            print(f"Seat {i}: {'Booked' if status == 1 else 'Available'}")
        print("========================")
def main():
    bus = Bus()
    while True:
        print("\n===== Bus Reservation Menu =====")
        print("1. Count Available Seats")
        print("2. Book a Seat")
        print("3. Cancel a Booking")
        print("4. Display Seat Status")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(f"Available Seats: {bus.count_available()}")
        elif choice == 2:
            seat_no = int(input("Enter seat number to book (1-20): "))
            bus.book_seat(seat_no)
        elif choice == 3:
            seat_no = int(input("Enter seat number to cancel (1-20): "))
            bus.cancel_booking(seat_no)
        elif choice == 4:
            bus.display_seats()
        elif choice == 5:
            print("Exiting Bus Reservation System...")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()
