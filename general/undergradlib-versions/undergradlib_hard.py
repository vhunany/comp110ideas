class UndergraduateLibrary:
    books: dict[str, dict[str, int]]  # Dictionary of genres and available books.
    tech: dict[str, int]              # Dictionary of tech equipment and their quantities.
    users: dict[str, list[str]]       # Dictionary of users and their checked-out items.

    def __init__(self, books: dict[str, dict[str, int]], tech: dict[str, int]) -> None:
        """
        Initialize the UndergraduateLibrary with books, tech, and users.

        :param books: A dictionary containing genres as keys, and another dictionary as values. 
                      This dictionary maps book names to available copies.
        :param tech: A dictionary containing tech names as keys and their available quantities as values.
        """
        self.books = books
        self.tech = tech
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
                found = False

                # Manual removal of the item without using .remove()
                for i in range(len(user_items)):
                    if user_items[i] == item:
                        found = True
                        # Remove the item by swapping with the last element and popping
                        user_items[i], user_items[-1] = user_items[-1], user_items[i]
                        user_items.pop()
                        break

                if found:
                    print(f"Checked in '{book_name}'. Thank you!")
                else:
                    print(f"No record of '{book_name}' being checked out by '{user}'.")
            else:
                print(f"No record of '{book_name}' being checked out by '{user}'.")
        else:
            print(f"'{book_name}' not found in {genre} genre.")

    def checkout_tech(self) -> None:
        """
        Prompt user to check out tech equipment from the library.
        """
        user = input("Enter your name: ")
        tech_name = input("Enter the name of the tech equipment to check out: ")

        if tech_name in self.tech:
            if self.tech[tech_name] > 0:
                self.tech[tech_name] -= 1

                # Add user entry if not present, and append tech details
                if user not in self.users:
                    self.users[user] = []
                self.users[user].append(f"Tech: '{tech_name}'")

                print(f"Checked out '{tech_name}'.")
            else:
                print(f"Sorry, '{tech_name}' is currently unavailable.")
        else:
            print(f"Sorry, '{tech_name}' not found in inventory.")

    def checkin_tech(self) -> None:
        """
        Prompt user to check in tech equipment to the library.
        """
        user = input("Enter your name: ")
        tech_name = input("Enter the name of the tech equipment to check in: ")

        if tech_name in self.tech:
            self.tech[tech_name] += 1

            # Check if user and tech entry exist, then remove it
            if user in self.users:
                item = f"Tech: '{tech_name}'"
                user_items = self.users[user]
                found = False

                # Manual removal of the item without using .remove()
                for i in range(len(user_items)):
                    if user_items[i] == item:
                        found = True
                        # Remove the item by swapping with the last element and popping
                        user_items[i], user_items[-1] = user_items[-1], user_items[i]
                        user_items.pop()
                        break

                if found:
                    print(f"Checked in '{tech_name}'. Thank you!")
                else:
                    print(f"No record of '{tech_name}' being checked out by '{user}'.")
            else:
                print(f"No record of '{tech_name}' being checked out by '{user}'.")
        else:
            print(f"'{tech_name}' not found in inventory.")

    def search_user(self, user: str) -> None:
        """
        Search for a user and print their checked-out items.

        :param user: The name of the user to search for.
        """
        if user in self.users:
            print(f"\nItems checked out by {user}:")
            for item in self.users[user]:
                print(f"- {item}")
        else:
            print(f"No records found for user '{user}'.")

    def __str__(self) -> str:
        """
        Return a string representation of the users and their checked-out items.
        """
        output = "\nUsers and Checked-Out Items:\n"
        for user in self.users:
            output += f"User: {user}\n"
            for item in self.users[user]:
                output += f"  - {item}\n"
        return output

    def receipt(self) -> None:
        """
        Print a receipt of all checked-out books and tech equipment.
        """
        if not any(len(items) for items in self.users.values()):
            print("No items have been checked out.")
        else:
            print("\nReceipt of Checked-Out Items:")
            print(self)  # Use the magic method __str__ for output


# Example Initialization
books = {
    "Fiction": {"The Great Gatsby": 5, "1984": 3},
    "Science": {"A Brief History of Time": 2, "The Selfish Gene": 4},
    "Technology": {"Clean Code": 1, "Design Patterns": 2},
}

tech = {
    "Laptop": 10,
    "Tablet": 5,
    "Camera": 3,
}

# Instantiate the library
library = UndergraduateLibrary(books, tech)

# Example Usage
library.checkout_book()  # Prompts for user and book details
library.checkin_book()   # Prompts for user and book details
library.checkout_tech()  # Prompts for user and tech details
library.checkin_tech()   # Prompts for user and tech details
library.search_user("Alice")  # Searches for a user's checked-out items
library.receipt()        # Prints out a receipt of checked-out items