class Library:
    def __init__(self):
        self._books = []  # Protected attribute to store the list of books

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def get_number_of_books(self):
        """Return the number of books in the library."""
        return len(self._books)

    def print_books(self):
        """Print all books in the library."""
        if self._books:
            print("Books in the library:")
            for book in self._books:
                print(f"- {book}")
        else:
            print("No books in the library.")

# Create an instance of Library
library = Library()

# Add books to the library
library.add_book("The Great Gatsby")
library.add_book("1984")
library.add_book("To Kill a Mockingbird")

# Print all books in the library
library.print_books()

# Get and print the number of books in the library
number_of_books = library.get_number_of_books()
print(f"Number of books in the library: {number_of_books}")

# At this point, if the program is stopped, the library's books are not persisted
