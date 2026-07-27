def search_book(book_ids, book_titles, book_copies, book_id):
    if book_id in book_ids:
        index = book_ids.index(book_id)
        title = book_titles[index]
        copies = book_copies[book_id]
        print(f"Book Found - ID: {book_id}, Title: {title}, Copies: {copies}")
    else:
        print(f"Book ID {book_id} not found.")
def display_books(book_ids, book_titles, book_copies):
    print("\nAvailable Books:")
    for i in range(len(book_ids)):
        if book_copies[book_ids[i]] > 0:
            print(f"ID: {book_ids[i]}, Title: {book_titles[i]}, Copies: {book_copies[book_ids[i]]}")
def main():
    book_ids = ["B101", "B102", "B103", "B104"]
    book_titles = ["Java Programming", "Python Basics", "Data Structures", "Operating Systems"]
    book_copies = {"B101": 3, "B102": 0, "B103": 5, "B104": 2}
    while True:
        print("\n--- Library Book Management ---")
        print("1. Search Book by ID")
        print("2. Display All Available Books")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            bid = input("Enter Book ID to search: ")
            search_book(book_ids, book_titles, book_copies, bid)
        elif choice == 2:
            display_books(book_ids, book_titles, book_copies)
        elif choice == 3:
            print("Exiting Library Book Management...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
