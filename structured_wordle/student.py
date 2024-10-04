
"""Wordle Game"""

__author__ = "730647349"


def input_guess(guess_num: int) -> str:
    guess: str = input(f"Enter a {guess_num} character word: ")
    while len(guess) != guess_num:
        guess = input(f"That wasn't {guess_num} chars! Try again: ")
    return guess


def contains_char(target_string: str, search_char: str) -> bool:
    """Determines the presence of a character within a word"""
    assert len(search_char) == 1
    count: int = 0
    index: int = 0
    while index <= len(
        target_string
    ):  # Searches the index of whatevr the target string is
        if target_string[index] == search_char:
            count += 1
        index += 1
    if count != 0:
        return True
    else:
        return False


def emojified(player_guess: str, secret_word: str) -> str:
    """Compares Player guess and secret word"""
    assert len(player_guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"  # emojis
    YELLOW_BOX: str = "\U0001F7E8"
    results: str = " "
    idx: int = 0
    while idx <= len(player_guess):
        if player_guess[idx] == secret_word[idx]:
            results += GREEN_BOX
        elif (
            contains_char(secret_word, player_guess[idx]) == True
        ):  # uses contain_char function to search for the target letter
            results += YELLOW_BOX
        else:
            results += WHITE_BOX
        idx = +1  # index should continuously increase
    return results


def main(secret: str) -> None:  # controls entrie game loops
    """Entrypoint of the program and main game loop."""
    turns_taken = 1
    max_turns = 6
    while turns_taken <= max_turns:
        print(f"=== Turn {turns_taken}/{max_turns} ===")
        guess = input_guess(len(secret))
        response = emojified(guess, secret)
        print(response)

        if guess == secret:
            print(f"You won in {turns_taken}/{max_turns} turns!")
            return
        turns_taken = +1
    print(f"X/{max_turns} - Sorry, try again tomorrow!")  # endgame scenario
    return


if __name__ == "__main__":
    main(secret="codes")