# Part 1. contains_char - 10 points
def contains_char(word: str, letter: str) -> bool: 
    assert len(letter) == 1

    tracker: bool = False
    idx: int = 0
    while idx < len(word): 
        if word[idx] == letter:
            tracker = True
        idx += 1
    
    return tracker


# Part 2. emojified - 20 points
def emojified(guess: str, secret: str) -> str: 
    assert len(guess) == len(secret)

    WHITE_BOX: str = "⬜"
    YELLOW_BOX: str = "🟨"
    GREEN_BOX: str = "🟩"

    idx: int = 0 
    emoji_result: str = ""

    while idx < len(guess):
        if guess[idx] == secret[idx]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
        idx += 1
    
    return emoji_result


# Part 3. input_guess – 10 Points
def input_guess(expected_length: int) -> str:
    guess = input(f"Enter a {expected_length} character word: ")
    
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    
    return guess

# Part 4. main – 30 Points
def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret = "codes"
    turn = 1
    won = False
    
    while turn <= 6 and not won:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))  # Prompt for a guess of the correct length
        result = emojified(guess, secret)  # Get the emoji codified result
        print(result)
        
        if guess == secret:
            won = True
        else:
            turn += 1
    
    if won:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
