'''# Library Management System (Unstructured Version)
# This code needs refactoring into a proper module with documentation.
library_db = {}
# Adding first book
title = "Python Basics"
author = "John Doe"
isbn = "101"
if isbn not in library_db:
library_db[isbn] = {"title": title, "author": author}
print("Book added successfully.")
else:
print("Book already exists.")
# Adding second book (duplicate logic)
title = "AI Fundamentals"
author = "Jane Smith"
isbn = "102"
if isbn not in library_db:
library_db[isbn] = {"title": title, "author": author}
print("Book added successfully.")
else:
print("Book already exists.")
# Searching book (repeated logic structure)
isbn = "101"
if isbn in library_db:
print("Book Found:", library_db[isbn])
else:
print("Book not found.")
# Removing book (again repeated pattern)
isbn = "101"
if isbn in library_db:
del library_db[isbn]
print("Book removed successfully.")
else:
print("Book not found.")
# Searching again
isbn = "101"
if isbn in library_db:
print("Book Found:", library_db[isbn])
else:
print("Book not found.")
use docstrings to document the functions and classes in the refactored code. This will help other developers understand the purpose and usage of each component in the library management system.
'''
class Library:
    """A simple library management system."""
    def __init__(self):
        """Initialize the library database."""
        self.library_db = {}
    def add_book(self, title, author, isbn):
        """
        Add a book to the library.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN number of the book.

        Returns:
            str: A message indicating whether the book was added successfully or if it already exists.
        """
        if isbn not in self.library_db:
            self.library_db[isbn] = {"title": title, "author": author}
            return "Book added successfully."
        else:
            return "Book already exists."
    def search_book(self, isbn):
        """
        Search for a book by its ISBN.

        Args:
            isbn (str): The ISBN number of the book to search for.
        Returns:
            str: A message indicating whether the book was found or not, along with the book details if found.
        """
        if isbn in self.library_db:
            return f"Book Found: {self.library_db[isbn]}"
        else:
            return "Book not found."
    def remove_book(self, isbn):
        """
        Remove a book from the library by its ISBN.

        Args:
            isbn (str): The ISBN number of the book to remove.
        Returns:
            str: A message indicating whether the book was removed successfully or if it was not found.
        """
        if isbn in self.library_db:
            del self.library_db[isbn]
            return "Book removed successfully."
        else:
            return "Book not found."
# Example usage:
if __name__ == "__main__":
    library = Library()
    print(library.add_book("Python Basics", "John Doe", "101"))
    print(library.add_book("AI Fundamentals", "Jane Smith", "102"))
    print(library.search_book("101"))
    print(library.remove_book("101"))
    print(library.search_book("101"))
    print(Library.add_book.__doc__)
