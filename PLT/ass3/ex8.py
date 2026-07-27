# Movie Ticket Booking System
class MovieTicket:
    def __init__(self, customer_name, movie_name, num_tickets, ticket_price):
        self.customer_name = customer_name
        self.movie_name = movie_name
        self.num_tickets = num_tickets
        self.ticket_price = ticket_price
    def calculate_total(self):
        return self.num_tickets * self.ticket_price
    def apply_discount(self):
        total = self.calculate_total()
        if self.num_tickets >= 5:
            discount = 0.15 * total
        elif 3 <= self.num_tickets <= 4:
            discount = 0.10 * total
        else:
            discount = 0
        return total - discount
    def display_summary(self):
        total = self.calculate_total()
        final_amount = self.apply_discount()
        print(f"Customer Name: {self.customer_name}")
        print(f"Movie Name: {self.movie_name}")
        print(f"Number of Tickets: {self.num_tickets}")
        print(f"Ticket Price: ₹{self.ticket_price}")
        print(f"Total Amount: ₹{total}")
        print(f"Final Bill after Discount: ₹{final_amount}")
        print("---------------")
booking1 = MovieTicket("Alice", "Inception", 2, 250)
booking2 = MovieTicket("Bob", "Interstellar", 4, 300)
booking3 = MovieTicket("Charlie", "The Dark Knight", 6, 200)
booking1.display_summary()
booking2.display_summary()
booking3.display_summary()
