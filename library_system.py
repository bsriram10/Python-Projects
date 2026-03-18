# Library Management System - Python OOPs
# Author: B. Sriram

class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = True

    def display_book(self):
        status = "Available" if self.is_available else "Not Available"
        print(f"  ID: {self.book_id} | Title: {self.title} | "
              f"Author: {self.author} | Status: {status}")


class Member:
    def __init__(self, member_name, member_id):
        self.member_name = member_name
        self.member_id = member_id
        self.borrowed_books = []

    def display_member(self):
        print(f"  ID: {self.member_id} | Name: {self.member_name}")
        if self.borrowed_books:
            print(f"  Borrowed Books: {', '.join(self.borrowed_books)}")
        else:
            print(f"  Borrowed Books: None")


class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to {self.library_name}.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.member_name}' registered successfully.")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_id):
        print("\n-- Borrow Request --")
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print(f"Member ID {member_id} not found!")
            return
        if not book:
            print(f"Book ID {book_id} not found!")
            return
        if not book.is_available:
            print(f"Sorry! '{book.title}' is currently not available.")
            return

        book.is_available = False
        member.borrowed_books.append(book.title)
        print(f"'{book.title}' successfully borrowed by {member.member_name}.")

    def return_book(self, member_id, book_id):
        print("\n-- Return Request --")
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if not member:
            print(f"Member ID {member_id} not found!")
            return
        if not book:
            print(f"Book ID {book_id} not found!")
            return
        if book.title not in member.borrowed_books:
            print(f"{member.member_name} has not borrowed '{book.title}'.")
            return

        book.is_available = True
        member.borrowed_books.remove(book.title)
        print(f"'{book.title}' successfully returned by {member.member_name}.")

    def display_all_books(self):
        print(f"\n========== ALL BOOKS IN {self.library_name.upper()} ==========")
        if not self.books:
            print("  No books available.")
        else:
            for book in self.books:
                book.display_book()
        print("=" * 50)

    def display_all_members(self):
        print(f"\n========== ALL MEMBERS ==========")
        if not self.members:
            print("  No members registered.")
        else:
            for member in self.members:
                member.display_member()
        print("=" * 35)


# Main Program
print("===== LIBRARY MANAGEMENT SYSTEM =====\n")

# Create Library
lib = Library("City Central Library")

# Add 5 Books
print("-- Adding Books --")
b1 = Book("Python Programming", "Guido van Rossum", "B001")
b2 = Book("Data Structures", "Mark Allen Weiss", "B002")
b3 = Book("Clean Code", "Robert C. Martin", "B003")
b4 = Book("The Pragmatic Programmer", "Andrew Hunt", "B004")
b5 = Book("Introduction to Algorithms", "Thomas H. Cormen", "B005")

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.add_book(b4)
lib.add_book(b5)

# Register 3 Members
print("\n-- Registering Members --")
m1 = Member("B. Sriram", "M001")
m2 = Member("Ravi Kumar", "M002")
m3 = Member("Priya Sharma", "M003")

lib.register_member(m1)
lib.register_member(m2)
lib.register_member(m3)

# Display all books before borrowing
lib.display_all_books()

# Borrow operations
lib.borrow_book("M001", "B001")
lib.borrow_book("M002", "B003")
lib.borrow_book("M003", "B001")  # Already borrowed - should show not available
lib.borrow_book("M001", "B005")

# Display members after borrowing
lib.display_all_members()

# Return operations
lib.return_book("M001", "B001")
lib.return_book("M002", "B002")  # Never borrowed - should show error

# Display final status of all books
lib.display_all_books()

# Display final member status
lib.display_all_members()

print("\n===== END OF LIBRARY SYSTEM =====")