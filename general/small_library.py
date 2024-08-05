# Function Definitions

def add_book(library, book_id, title):
    if book_id in library:
        print("Book ID already exists.")
    else:
        library[book_id] = {'title': title, 'available': True}
        print(f"Book '{title}' added to the library.")

def borrow_book(library, book_id):
    if book_id in library:
        if library[book_id]['available']:
            library[book_id]['available'] = False
            print(f"You have borrowed '{library[book_id]['title']}'.")
        else:
            print(f"Book '{library[book_id]['title']}' is already borrowed.")
    else:
        print("Book ID not found.")

def return_book(library, book_id):
    if book_id in library:
        if not library[book_id]['available']:
            library[book_id]['available'] = True
            print(f"You have returned '{library[book_id]['title']}'.")
        else:
            print(f"Book '{library[book_id]['title']}' was not borrowed.")
    else:
        print("Book ID not found.")

def list_available_books(library):
    available_books = [book for book in library.values() if book['available']]
    if available_books:
        print("Available books:")
        for book in available_books:
            print(f"- {book['title']}")
    else:
        print("No books are currently available.")

# Main Program

library = {}

while True:
    print("\nLibrary Menu:")
    print("1. Add a book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. List available books")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        add_book(library, book_id, title)
    elif choice == '2':
        book_id = input("Enter book ID to borrow: ")
        borrow_book(library, book_id)
    elif choice == '3':
        book_id = input("Enter book ID to return: ")
        return_book(library, book_id)
    elif choice == '4':
        list_available_books(library)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
