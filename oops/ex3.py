# Library Book Management System
class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__available_copies = available_copies
    def issue_book(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
            print(f"Book '{self.__title}' issued successfully.")
        else:
            print("Book Not Available")
    def return_book(self):
        self.__available_copies += 1
        print(f"Book '{self.__title}' returned successfully.")
    def display_details(self):
        print("===================================")
        print(f"Book ID           : {self.__book_id}")
        print(f"Title             : {self.__title}")
        print(f"Author            : {self.__author}")
        print(f"Available Copies  : {self.__available_copies}")
        print("===================================")
def main():
    book1 = Book(101, "Python Programming", "John Smith", 2)
    book2 = Book(102, "Data Science Essentials", "Alice Brown", 0)
    book1.display_details()
    book2.display_details()
    book1.issue_book()
    book1.display_details()
    book2.issue_book()
    book1.return_book()
    book1.display_details()
if __name__ == "__main__":
    main()
