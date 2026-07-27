# Library Book Borrowing System
class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies
    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"Book '{self.title}' borrowed successfully.")
        else:
            print("Book Currently Unavailable")
    def return_book(self):
        self.available_copies += 1
        print(f"Book '{self.title}' returned successfully.")
    def display_availability(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available Copies: {self.available_copies}")
        print("---------------")
book1 = Book(101, "Python Programming", "John Smith", 2)
book2 = Book(102, "Data Science Essentials", "Alice Brown", 0)
book1.display_availability()
book1.borrow_book()
book1.display_availability()
book2.display_availability()
book2.borrow_book()  
book2.return_book()
book2.display_availability()
