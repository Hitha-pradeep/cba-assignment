def analyze_bookings(bookings):
    max_bookings = max(bookings)
    max_show = bookings.index(max_bookings) + 1
    min_bookings = min(bookings)
    min_show = bookings.index(min_bookings) + 1
    total = sum(bookings)
    average = total / len(bookings)
    print("===================================")
    print(f"Bookings per Show   : {bookings}")
    print(f"Most Booked Show    : Show {max_show} ({max_bookings} tickets)")
    print(f"Least Booked Show   : Show {min_show} ({min_bookings} tickets)")
    print(f"Total Tickets Sold  : {total}")
    print(f"Average per Show    : {average:.2f}")
    print("===================================")
def main():
    bookings = []
    n = int(input("Enter number of shows: "))
    for i in range(n):
        tickets = int(input(f"Enter tickets booked for Show {i+1}: "))
        bookings.append(tickets)
    analyze_bookings(bookings)
if __name__ == "__main__":
    main()
