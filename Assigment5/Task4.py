class LibraryBook:
    def __init__(self, book_id, title, author, borrower, days_late):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.borrower = borrower
        self.days_late = days_late

    def display_details(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Borrower: {self.borrower}")
        print(f"Days Late: {self.days_late}")

    def calculate_late_fee(self):
        if self.days_late <= 5:
            fee_per_day = 5
        elif 6 <= self.days_late <= 10:
            fee_per_day = 7
        else:
            fee_per_day = 10
        total_fee = self.days_late * fee_per_day
        return total_fee
# Creating an instance of LibraryBook
book = LibraryBook(book_id=1, title="The Great Gatsby", author="F. Scott Fitzgerald",
                   borrower="John Doe", days_late=8)
# Displaying book details
book.display_details()
# Calculating and printing late fee
late_fee = book.calculate_late_fee()
print(f"Late Fee: ₹{late_fee}")
# Analysis:
# Time Complexity: O(1) - Both methods perform a constant number of operations.