const library = {
  books: [
    { title: "JavaScript", available: true },
    { title: "Python", available: false },
    { title: "Java", available: true }
  ]
};

const availableBooks = library.books.filter(book => book.available);
console.log("Available Books:", availableBooks);

library.books.push({ title: "C++", available: true });
console.log("After Adding New Book:", library.books);

const pythonBook = library.books.find(book => book.title === "Python");
if (pythonBook) {
  pythonBook.available = true;
}
console.log("After Updating Python Availability:", library.books);
const bookTitles = library.books.map(book => book.title);
console.log("Book Titles:", bookTitles);
