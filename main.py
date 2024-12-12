"""Creating a Library Mangement System That Easy to borrow and return """
class Library:     # Create the Library class
    book_list = []

    @classmethod
    def entry_book(self, book):
        self.book_list.append(book)


class Book:  # Create the Book class & Initialize Object
    def __init__(self, title, author, avilability):
        self.__book_id = len(Library.book_list) + 100
        self.__title = title
        self.__author = author
        self.__availability = avilability
        Library.entry_book(self)

    def borrow_book(self):  # Implement borrow_book() method
        print("\n")
        if self.__availability == 'Available':
            print(f'The book "{self.__title}"is borrowed Successfully!!')
            self.__availability = 'Not Available'
        else:
            print(f'Now,This book is Not Available !!')

    def return_book(self):     # Implement return_book() method
        if self.__availability != 'Available':
            print("Thank's For Return Book !!")
        else:
            print(f'The book Already Available in Library !!')

    def view_book_info(self):  # Implement view_book_info() method
        print(f"Book ID: {self.__book_id} Title: \"{self.__title}\" Author: {
              self.__author} Availability: {self.__availability}")

    def get_book_id(self):  # Data Privacy
        return self.__book_id

    def get_title(self):  # Data Privacy
        return self.__title

    def get_author(self):  # Data Privacy
        return self.__author

    def get_availability(self):  # Data Privacy
        return self.__availability


def menu():            # Menu System &  Error Handling
    while True:
        print("\n-----------welcome to the Library--------------")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit\n")

        choice = int(input("Choose an option: "))

        if choice == 1:
            if Library.book_list:
                print("\n-----------List of Books:-------------")
                for book in Library.book_list:
                    book.view_book_info()
            else:
                print("No books available.")

        elif choice == 2:
            book_id = int(input("Enter the Book ID to borrow: "))
            found = False
            for book in Library.book_list:
                if book.get_book_id() == book_id:
                    found = True
                    book.borrow_book()
                    break
            if not found:
                print(f"Error: Book with ID {book_id} not found.")

        elif choice == 3:
            book_id = int(input("Enter the Book ID to return: "))
            found = False
            for book in Library.book_list:
                if book.get_book_id() == book_id:
                    found = True
                    book.return_book()
                    break
            if not found:
                print(f"Error: Book with ID {book_id} not found.")

        elif choice == 4:
            print("Successfully exited.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")


# Creating Book objects
book1 = Book("1984", "George Orwell", "Available")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Available")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Available")
book4 = Book("The Catcher in the Rye", "J.D. Salinger", "Available")
book5 = Book("Pride and Prejudice", "Jane Austen", "Available")
book6 = Book("The Hobbit", "J.R.R. Tolkien", "Available")
book7 = Book("Brave New World", "Aldous Huxley", "Available")
book8 = Book("Fahrenheit 451", "Ray Bradbury", "Available")
book9 = Book("Moby Dick", "Herman Melville", "Available")
book10 = Book("War and Peace", "Leo Tolstoy", "Available")

# Viewing all books in the library


menu()
