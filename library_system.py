class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = True  # Defaults to True when a book is created

    def display_book(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"[{self.book_id}] '{self.title}' by {self.author} - Status: {status}")


class Member:
    def __init__(self, member_name, member_id):
        self.member_name = member_name
        self.member_id = member_id
        self.borrowed_books = []  # Starts with an empty list

    def display_member(self):
        # Extract titles from the list of Book objects for a cleaner display
        books_list = [book.title for book in self.borrowed_books]
        borrowed_str = ", ".join(books_list) if books_list else "None"
        print(f"Member [{self.member_id}]: {self.member_name} | Borrowed: {borrowed_str}")


class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_id, book_id):
        # Helper to find the specific member and book using list comprehensions/generators
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if not member:
            print(f"Error: Member ID {member_id} not found.")
            return
        if not book:
            print(f"Error: Book ID {book_id} not found.")
            return

        if book.is_available:
            book.is_available = False
            member.borrowed_books.append(book)
            print(f"Success: {member.member_name} borrowed '{book.title}'.")
        else:
            print(f"Sorry: '{book.title}' is currently not available.")

    def return_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if not member or not book:
            print("Error: Invalid Member ID or Book ID.")
            return

        if book in member.borrowed_books:
            book.is_available = True
            member.borrowed_books.remove(book)
            print(f"Success: {member.member_name} returned '{book.title}'.")
        else:
            print(f"Error: {member.member_name} does not currently have '{book.title}' borrowed.")

    def display_all_books(self):
        print(f"\n--- All Books in {self.library_name} ---")
        for book in self.books:
            book.display_book()

    def display_all_members(self):
        print(f"\n--- All Members in {self.library_name} ---")
        for member in self.members:
            member.display_member()

if __name__ == "__main__":
    city_library = Library("City Central Library")

    book1 = Book("1984", "George Orwell", "B01")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "B02")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "B03")
    book4 = Book("Pride and Prejudice", "Jane Austen", "B04")
    book5 = Book("Dune", "Frank Herbert", "B05")

    for b in [book1, book2, book3, book4, book5]:
        city_library.add_book(b)

    
    member1 = Member("Alice Smith", "M01")
    member2 = Member("Bob Jones", "M02")
    member3 = Member("Charlie Brown", "M03")

    for m in [member1, member2, member3]:
        city_library.register_member(m)

    
    print("--- Borrowing Operations ---")
    city_library.borrow_book("M01", "B01")  
    city_library.borrow_book("M02", "B03")  
    city_library.borrow_book("M03", "B01")  

    print("\n--- Return Operations ---")
    city_library.return_book("M01", "B01")  
    city_library.borrow_book("M03", "B01")  

    
    city_library.display_all_books()
    city_library.display_all_members()