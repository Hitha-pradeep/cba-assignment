from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# ------------------- Book -------------------
class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__issued = False
        self.__reserved_by = None

    def get_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_issued(self):
        return self.__issued

    def set_issued(self, status):
        self.__issued = status

    def reserve(self, member):
        self.__reserved_by = member

    def get_reserved_by(self):
        return self.__reserved_by


# ------------------- Member -------------------
class Member:
    MAX_BOOKS = 3

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def can_borrow(self):
        return len(self.borrowed_books) < Member.MAX_BOOKS


# ------------------- Transaction -------------------
class Transaction:
    FINE_PER_DAY = 5

    def __init__(self, member, book):
        self.member = member
        self.book = book
        self.issue_date = datetime.now()
        self.due_date = self.issue_date + timedelta(days=7)

    def calculate_fine(self):
        today = datetime.now()
        if today > self.due_date:
            days = (today - self.due_date).days
            return days * Transaction.FINE_PER_DAY
        return 0


# ------------------- Abstract Librarian -------------------
class Librarian(ABC):

    @abstractmethod
    def issue_book(self, library, member_id, book_id):
        pass

    @abstractmethod
    def return_book(self, library, member_id, book_id):
        pass


# ------------------- Library -------------------
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def search_by_title(self, title):
        for book in self.books:
            if title.lower() in book.get_title().lower():
                print(book.get_title(), "-", book.get_author())

    def search_by_author(self, author):
        for book in self.books:
            if author.lower() in book.get_author().lower():
                print(book.get_title(), "-", book.get_author())

    def get_book(self, book_id):
        for book in self.books:
            if book.get_id() == book_id:
                return book
        return None

    def get_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None


# ------------------- Library Staff -------------------
class LibraryStaff(Librarian):

    def issue_book(self, library, member_id, book_id):
        try:
            member = library.get_member(member_id)
            book = library.get_book(book_id)

            if member is None:
                raise Exception("Member not found.")

            if book is None:
                raise Exception("Book not found.")

            if not member.can_borrow():
                raise Exception("Maximum 3 books allowed.")

            if book.is_issued():
                raise Exception("Book already issued.")

            if book.get_reserved_by() is not None and book.get_reserved_by() != member:
                raise Exception("Book is reserved by another member.")

            book.set_issued(True)
            member.borrowed_books.append(book)

            transaction = Transaction(member, book)
            library.transactions.append(transaction)

            print("Book Issued Successfully")

        except Exception as e:
            print("Error:", e)

    def return_book(self, library, member_id, book_id):
        try:
            member = library.get_member(member_id)
            book = library.get_book(book_id)

            if member is None or book is None:
                raise Exception("Invalid member/book.")

            transaction = None

            for t in library.transactions:
                if t.member == member and t.book == book:
                    transaction = t
                    break

            if transaction is None:
                raise Exception("Transaction not found.")

            fine = transaction.calculate_fine()

            book.set_issued(False)
            member.borrowed_books.remove(book)
            library.transactions.remove(transaction)

            print("Book Returned Successfully")
            print("Fine = ₹", fine)

        except Exception as e:
            print("Error:", e)


# ------------------- Main -------------------
library = Library()
staff = LibraryStaff()

# Add Books
library.add_book(Book(1, "Python Programming", "Guido"))
library.add_book(Book(2, "Data Structures", "Mark Allen"))
library.add_book(Book(3, "Machine Learning", "Andrew Ng"))

# Register Members
library.register_member(Member(101, "Alice"))
library.register_member(Member(102, "Bob"))

# Reserve Book 3 for Alice
book = library.get_book(3)
member = library.get_member(101)
book.reserve(member)

# Search
print("Books by Title:")
library.search_by_title("Python")

print("\nBooks by Author:")
library.search_by_author("Andrew")

# Issue
print("\nIssue Book:")
staff.issue_book(library, 101, 1)

# Try issuing reserved book to another member
print("\nReserved Book Test:")
staff.issue_book(library, 102, 3)

# Return
print("\nReturn Book:")
staff.return_book(library, 101, 1)