# ---------------- Movie ----------------
class Movie:
    def __init__(self, title, timings):
        self.title = title
        self.timings = timings

# ---------------- Seat ----------------
class Seat:
    def __init__(self, seat_no):
        self.__seat_no = seat_no
        self.__booked = False

    def is_booked(self):
        return self.__booked

    def book(self):
        self.__booked = True

    def cancel(self):
        self.__booked = False

    def get_no(self):
        return self.__seat_no

# ---------------- Screen ----------------
class Screen:
    def __init__(self, screen_no, total_seats):
        self.screen_no = screen_no
        self.seats = [Seat(i + 1) for i in range(total_seats)]

    def display_available_seats(self):
        print("Available Seats:")
        for seat in self.seats:
            if not seat.is_booked():
                print(seat.get_no(), end=" ")
        print()

# ---------------- Theater ----------------
class Theater:
    def __init__(self, name):
        self.name = name
        self.movies = []
        self.screens = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def add_screen(self, screen):
        self.screens.append(screen)

    def display_movies(self):
        print("\nMovies & Show Timings")
        for movie in self.movies:
            print(movie.title, "->", ", ".join(movie.timings))

# ---------------- Customer ----------------
class Customer:
    def __init__(self, name):
        self.name = name

    def get_discount(self):
        return 0

class Student(Customer):
    def get_discount(self):
        return 0.20      # 20%

class SeniorCitizen(Customer):
    def get_discount(self):
        return 0.30      # 30%

# ---------------- Payment ----------------
class Payment:
    def pay(self, amount):
        print("Online Payment Successful")
        print("Amount Paid: ₹", amount)

# ---------------- Booking ----------------
class Booking:
    BASE_PRICE = 200

    def __init__(self, customer, screen):
        self.customer = customer
        self.screen = screen
        self.payment = Payment()

    def book_ticket(self, seat_no):
        seat = self.screen.seats[seat_no - 1]

        if seat.is_booked():
            print("Seat Already Booked!")
            return

        seat.book()

        # Dynamic pricing
        price = Booking.BASE_PRICE
        if seat_no <= 5:
            price = 300

        discount = price * self.customer.get_discount()
        final_price = price - discount

        self.payment.pay(final_price)

        print("\n----- Ticket -----")
        print("Customer :", self.customer.name)
        print("Seat :", seat_no)
        print("Ticket Price : ₹", final_price)
        print("------------------")

    def cancel_ticket(self, seat_no):
        seat = self.screen.seats[seat_no - 1]

        if seat.is_booked():
            seat.cancel()
            print("Ticket Cancelled")
        else:
            print("Seat is already available")

# ---------------- Main ----------------
theater = Theater("PVR")

movie = Movie("Avengers", ["10:00 AM", "2:00 PM", "6:00 PM"])
theater.add_movie(movie)

screen = Screen(1, 10)
theater.add_screen(screen)

# Display Movies
theater.display_movies()

# Available Seats
screen.display_available_seats()

# Student Booking
student = Student("Alice")
booking1 = Booking(student, screen)
booking1.book_ticket(2)

# Senior Citizen Booking
senior = SeniorCitizen("Bob")
booking2 = Booking(senior, screen)
booking2.book_ticket(6)

# Double Booking Test
booking2.book_ticket(2)

# Available Seats
screen.display_available_seats()

# Cancel Ticket
booking1.cancel_ticket(2)

# Available Seats Again
screen.display_available_seats()