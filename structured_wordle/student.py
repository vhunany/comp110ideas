
"""Creating a Wordle"""

__author__ = "730754065"


def input_guess(secret_word_len: int) -> str:
    """Create a function that make sure the word gussed and the secret number are same length"""
    word = secret_word_len
    guess: str = input(f"Enter a {word} character word: ")
    # Ask the user to enter a cetain characters of word
    while word != len(guess):
        # Keep on asking the user to enter a certain amount of character word
        print(f"That wasn't a {word} character word! Try again: {guess}")
        guess = input()
    return guess


def contains_char(searched_word: str, searching_letter: str) -> bool:
    """Return ture if character is found in word, else, return false"""
    assert len(searching_letter) == 1
    x: int = 0
    z: int = 0
    # set 2 local vaibles to help check if a letter is in a word
    while x < len(searched_word):
        if searched_word[x] == searching_letter:
            z += 1
        x += 1
    return bool(z > 0)


def emojified(guessed_word: str, secret_word: str) -> str:
    """Compare string of equal lenght, the secret and gussed word"""
    assert len(guessed_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    x: int = 0
    y: str = ""
    # Create varibles so while loop can run and the results can be returned together
    while x < len(guessed_word):
        if guessed_word[x] == secret_word[x]:
            y += GREEN_BOX
            x += 1
        elif contains_char(secret_word, guessed_word[x]) == True:
            y += YELLOW_BOX
            x += 1
        else:
            y += WHITE_BOX
            x += 1
    # assigning colors to letters that were right, in the wrong place, and wrong
    return y


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    print(f"=== Turn {turn}/6 ===")
    turn += 1
    guess: str = input_guess(len(secret))
    emojified(guess, secret)
    # ask the user to give a guess
    while turn <= 6:
        print(emojified(guess, secret))
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        if turn < 6:
            if guess == secret:
                print(f"You won in {turn}/6 turns!")
        elif turn == 6:
            print("X/6 - Sorry, try again tomorrow!")
        turn += 1


if __name__ == "__main__":
    main(secret="codes")