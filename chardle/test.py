
"""EX02 - Chardle"""

__author__ = "730467230"


def input_word() -> str:
    """Function prompting for five letter word"""
    word = input("Enter a 5-character word: ")
    if len(word) == int(5):
        print(word)
    else:
        print("Error: Word must contain 5 characters")
        exit()
    return word


def input_letter() -> str:
    """Function prompting for single character"""
    letter = input("Enter a single character: ")
    if len(letter) == int(1):
        print(letter)
    else:
        print("Character must be a single character")
        exit()
    return letter


def contains_char(word=input_word(), letter=input_letter()) -> None:
    "Function to see how many letters are in the word and what indexes they are located in"
    print("Searching for " + letter + " in " + word)
    """Using count variable to see how many instaces of letter were found"""
    count = 0
    """using if statements for each index"""
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    if count == 1:
        print("1 instance of " + letter + " found in " + word)
    elif count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)


def main() -> None:
    """Calling all the functions"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    """Calling main function"""
    main()
