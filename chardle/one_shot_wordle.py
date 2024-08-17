def input_word() -> str:
    """Prompts the user for a 5-character word."""
    word_guess = input("Enter a 5-character word: ")
    if len(word_guess) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word_guess

def input_letter() -> str:
    """Prompts the user for a single character."""
    letter_guess = input("Enter a single character: ")
    if len(letter_guess) != 1:
        print("Error: Character must be a single character.")
        exit()
    return letter_guess

def contains_char(word_guess: str, letter_guess: str) -> None:
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


    if counter == 1:
            print(f"{counter} instance of {letter_guess} found in {word_guess}")

    if counter > 1:
        print(f"{counter} instances of {letter_guess} found in {word_guess}")

    if counter == 0:
        print(f"No instances of {letter_guess} found in {word_guess}")

def main() -> None:
    """Main function to run the Chardle game."""
    word = input_word()
    letter = input_letter()
    contains_char(word, letter)

# main()