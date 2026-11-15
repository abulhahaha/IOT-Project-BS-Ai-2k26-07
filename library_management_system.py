class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity
        self.available_quantity = quantity


class Library:
    def __init__(self):
        # Dictionary stores books using their unique IDs.
        self.books = {}

        # List stores the details of every issued copy.
        self.issued_books = []

    def add_book(self):
        print("\nADD NEW BOOK")
        book_id = input("Enter Book ID: ").strip()

        if not book_id:
            print("Book ID cannot be empty.")
            return

        if book_id in self.books:
            print("A book with this ID already exists.")
            return

        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()

        if not title or not author:
            print("Book title and author name cannot be empty.")
            return

        try:
            quantity = int(input("Enter Quantity: "))
            if quantity <= 0:
                print("Book quantity must be a positive whole number.")
                return
        except ValueError:
            print("Please enter a valid whole number for quantity.")
            return

        self.books[book_id] = Book(book_id, title, author, quantity)
        print("Book added successfully!")

    def view_all_books(self):
        print("\nALL BOOKS")

        if not self.books:
            print("No books are available in the library record.")
            return

        for book in self.books.values():
            print("-----------------------------------")
            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Total Quantity:", book.quantity)
            print("Available Quantity:", book.available_quantity)

    def search_book(self):
        print("\nSEARCH BOOK")
        search_value = input("Enter Book ID or Book Title: ").strip()

        if not search_value:
            print("Please enter a book ID or title.")
            return

        # First check whether the entered value is a book ID.
        if search_value in self.books:
            self.display_book(self.books[search_value])
            return

        # If it is not an ID, search by title without case sensitivity.
        found = False
        for book in self.books.values():
            if search_value.lower() in book.title.lower():
                self.display_book(book)
                found = True

        if not found:
            print("Book not found.")

    def display_book(self, book):
        print("-----------------------------------")
        print("Book ID:", book.book_id)
        print("Title:", book.title)
        print("Author:", book.author)
        print("Total Quantity:", book.quantity)
        print("Available Quantity:", book.available_quantity)

    def issue_book(self):
        print("\nISSUE BOOK")
        book_id = input("Enter Book ID: ").strip()

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]

        if book.available_quantity == 0:
            print("This book is currently unavailable.")
            return

        student_name = input("Enter Student Name: ").strip()

        if not student_name:
            print("Student name cannot be empty.")
            return

        # Save the student and book details, then reduce available copies.
        self.issued_books.append({
            "book_id": book_id,
            "book_title": book.title,
            "student_name": student_name
        })

        book.available_quantity -= 1
        print("Book issued successfully!")
        print("Available Quantity:", book.available_quantity)

    def return_book(self):
        print("\nRETURN BOOK")
        book_id = input("Enter Book ID: ").strip()
        student_name = input("Enter Student Name: ").strip()

        if book_id not in self.books:
            print("Book not found.")
            return

        if not student_name:
            print("Student name cannot be empty.")
            return

        # A return is accepted only if this student has this book issued.
        for index, record in enumerate(self.issued_books):
            if (record["book_id"] == book_id and
                    record["student_name"].lower() == student_name.lower()):

                self.issued_books.pop(index)
                self.books[book_id].available_quantity += 1
                print("Book returned successfully!")
                print("Available Quantity:",
                      self.books[book_id].available_quantity)
                return

        print("No matching issued book record was found for this student.")

    def delete_book(self):
        print("\nDELETE BOOK")
        book_id = input("Enter Book ID: ").strip()

        if book_id not in self.books:
            print("Book not found.")
            return

        # Do not delete a book if any copy is currently issued.
        for record in self.issued_books:
            if record["book_id"] == book_id:
                print("This book cannot be deleted because a copy is issued.")
                return

        del self.books[book_id]
        print("Book record deleted successfully!")

    def view_issued_books(self):
        print("\nISSUED BOOKS")

        if not self.issued_books:
            print("There are currently no issued books.")
            return

        for number, record in enumerate(self.issued_books, start=1):
            print("-----------------------------------")
            print("Record:", number)
            print("Book ID:", record["book_id"])
            print("Book Title:", record["book_title"])
            print("Student Name:", record["student_name"])

    def run(self):
        # The while loop keeps showing the menu until the user selects Exit.
        while True:
            print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
            print("1. Add Book")
            print("2. View All Books")
            print("3. Search Book")
            print("4. Issue Book")
            print("5. Return Book")
            print("6. Delete Book")
            print("7. View Issued Books")
            print("8. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.view_all_books()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.issue_book()
            elif choice == "5":
                self.return_book()
            elif choice == "6":
                self.delete_book()
            elif choice == "7":
                self.view_issued_books()
            elif choice == "8":
                print("Thank you for using the Library Management System.")
                print("Program closed safely.")
                break
            else:
                print("Invalid choice. Please select a number from 1 to 8.")


# Create a Library object and start the program.
library = Library()
library.run()
