"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "1234567890"

word_guess: str = input("Enter a 5-character word: ")

if len(word_guess) != 5: 
    print("Error: Word must contain 5 characters")

letter_guess: str = input("Enter a single character: ")

if len(letter_guess) != 1: 
    print("Error: Character must be a single character.")


print(f"Searching for {letter_guess} in {word_guess}")


"""
 For now, you will need to check each of the five indices of 
 the word string to see if it is equal to the character string. 
 If so, then you should print out a message indicating the letter 
 being searched for was found at a given index. Your goal in this 
 part is to be able to do the following:
"""
counter: int = 0

if word_guess[0] == letter_guess: 
    print(f"{letter_guess} found at index 0")
    counter += 1

if word_guess[1] == letter_guess: 
    print(f"{letter_guess} found at index 1")
    counter += 1 

if word_guess[2] == letter_guess: 
    print(f"{letter_guess} found at index 2")
    counter += 1

if word_guess[3] == letter_guess: 
    print(f"{letter_guess} found at index 3")
    counter += 1

if word_guess[4] == letter_guess: 
    print(f"{letter_guess} found at index 4")
    counter += 1

if counter != 0: 
    print(f"{counter} instances of {letter_guess} found in heels")
else: 
    print(f"No instances of {letter_guess} found in heels")



def input_guess() -> str: 
    return input("Enter a 5-character word: ")

def letter_guess() -> str: 
    return input("Enter a single character: ")





# print(f"Searching for {letter_guess} in {word_guess}")

# def input_guess() -> str: 
#     return input("Enter a 5-character word: ")

# def letter_guess() -> str: 
#     return input("Enter a single character: ")


# For now, you will need to check each of the five indices of 
# the word string to see if it is equal to the character string. 
# If so, then you should print out a message indicating the letter 
# being searched for was found at a given index. Your goal in this 
# part is to be able to do the following:


# if input_guess()[0] == letter_guess(): 


def input_guess() -> str:
    """Prompts the user for a 5-character word."""
    word_guess = input("Enter a 5-character word: ")
    if len(word_guess) != 5:
        print("Error: Word must contain 5 characters.")
    return word_guess

def input_letter() -> str:
    """Prompts the user for a single character."""
    letter_guess = input("Enter a single character: ")
    if len(letter_guess) != 1:
        print("Error: Character must be a single character.")
    return letter_guess

def search_letter_in_word(word_guess: str, letter_guess: str) -> None:
    """Searches for the letter in the word and prints where it is found."""
    print(f"Searching for {letter_guess} in {word_guess}")
    counter = 0

    if word_guess[0] == letter_guess:
        print(f"{letter_guess} found at index 0")
        counter += 1

    if word_guess[1] == letter_guess:
        print(f"{letter_guess} found at index 1")
        counter += 1

    if word_guess[2] == letter_guess:
        print(f"{letter_guess} found at index 2")
        counter += 1

    if word_guess[3] == letter_guess:
        print(f"{letter_guess} found at index 3")
        counter += 1

    if word_guess[4] == letter_guess:
        print(f"{letter_guess} found at index 4")
        counter += 1

    if counter != 0:
        print(f"{counter} instances of {letter_guess} found in {word_guess}")
    else:
        print(f"No instances of {letter_guess} found in {word_guess}")

def chardle() -> None:
    """Main function to run the Chardle game."""
    word = input_guess()
    letter = input_letter()
    search_letter_in_word(word, letter)

chardle()
