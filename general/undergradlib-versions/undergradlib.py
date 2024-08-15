"""Mini Undergraduate Library Simulation!"""


class UndergraduateLibrary:
    books: dict[str, dict[str, int]]  # Dictionary of genres and available books.
    users: dict[str, list[str]]       # Dictionary of users and their checked-out items.

    def __init__(self, books: dict[str, dict[str, int]]) -> None:
        """
        Initialize the UndergraduateLibrary with books, tech, and users.

        :param books: A dictionary containing genres as keys, and another dictionary as values. 
                      This dictionary maps book names to available copies.
        :param tech: A dictionary containing tech names as keys and their available quantities as values.
        """
        self.books = books
        self.users = {}  # Initialize an empty dictionary for users

    def checkout_book(self) -> None:
        """
        Prompt user to check out a book from the library.
        """
        user = input("Enter your name: ")
        genre = input("Enter the genre of the book: ")
        book_name = input("Enter the name of the book to check out: ")

        if genre in self.books and book_name in self.books[genre]:
            if self.books[genre][book_name] > 0:
                self.books[genre][book_name] -= 1

                # Add user entry if not present, and append book details
                if user not in self.users:
                    self.users[user] = []
                self.users[user].append(f"Book: '{book_name}' in Genre: '{genre}'")

                print(f"Checked out '{book_name}'. Enjoy reading!")
            else:
                print(f"Sorry, '{book_name}' is currently unavailable.")
        else:
            print(f"Sorry, '{book_name}' not found in {genre} genre.")

    def checkin_book(self) -> None:
        """
        Prompt user to check in a book to the library.
        """
        user = input("Enter your name: ")
        genre = input("Enter the genre of the book: ")
        book_name = input("Enter the name of the book to check in: ")

        if genre in self.books and book_name in self.books[genre]:
            self.books[genre][book_name] += 1

            # Check if user and book entry exist, then remove it
            if user in self.users:
                item = f"Book: '{book_name}' in Genre: '{genre}'"
                user_items = self.users[user]
                found_index = -1

                # Search for the item and record its index
                for i in range(len(user_items)):
                    if user_items[i] == item:
                        found_index = i  # Instead of breaking the loop, we store the index of the found item in found_index.
                        # After the loop, if found_index is not -1, we know the item was found. We then perform the swap and remove operations.
                        # If found_index remains -1, it means the item was not found, and the appropriate message is printed.

                # If the item was found, perform the swap and remove operation
                if found_index != -1:
                    temp = user_items[found_index]  # Temporary variable
                    user_items[found_index] = user_items[-1]
                    user_items[-1] = temp
                    user_items.pop()
                    print(f"Checked in '{book_name}'. Thank you!")
                else:
                    print(f"No record of '{book_name}' being checked out by '{user}'.")
            else:
                print(f"No record of '{book_name}' being checked out by '{user}'.")
        else:
            print(f"'{book_name}' not found in {genre} genre.")


    def search_user(self, user: str) -> None:
        """
        Search for a user and print their checked-out items.

        :param user: The name of the user to search for.
        """
        if user in self.users:
            print(f"Items checked out by {user}:")
            for item in self.users[user]:
                print(f"- {item}")
        else:
            print(f"No records found for user '{user}'.")

    def __str__(self) -> str:
        """
        Return a string representation of the users and their checked-out items.
        """
        output = "Users and Checked-Out Items:"
        for user in self.users:
            output += f"User: {user}"
            for item in self.users[user]:
                output += f"  - {item}"
        return output

    def receipt(self) -> None:
        """
        Print a receipt of all checked-out books and tech equipment.
        """
        all_empty = True
        for user in self.users:
            items = self.users[user]
            if len(items) > 0:
                all_empty = False

        if all_empty:
            print("No items have been checked out.")
        else:
            print("Receipt of Checked-Out Items:")
            print(self)  # Use the magic method __str__ for output


# Example Initialization
books = {
    "Fiction": {"The Great Gatsby": 5, "1984": 3},
    "Science": {"A Brief History of Time": 2, "The Selfish Gene": 4},
    "Technology": {"Clean Code": 1, "Design Patterns": 2},
}

# Instantiate the library
library = UndergraduateLibrary(books)

# Example Usage
library.checkout_book()  # Prompts for user and book details
library.checkin_book()   # Prompts for user and book details
library.search_user("Alice")  # Searches for a user's checked-out items
library.receipt()        # Prints out a receipt of checked-out items
