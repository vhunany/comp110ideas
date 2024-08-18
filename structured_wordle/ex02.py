
# Part 1. Establishing a Secret and Prompting for a Guess – 30 Points
secret_word: str = "python"

guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

while len(guess) != 6: 
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")


# Part 2. Checking Indices for Correct Matches – 30 Points

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

idx: int = 0
result: str = ""

while idx < len(secret_word): 
    if guess[idx] == secret_word[idx]: 
        result += GREEN_BOX
    else: 
        # Part 3. Checking Other Indices for Correct Letters at Incorrect Positions – 10 Points
        bool_var: bool = False
        alt_idx: int = 0
        while bool_var == False and alt_idx < len(secret_word): 
            if secret_word[alt_idx] == guess[idx]:
                bool_var = True
            else: 
                alt_idx += 1
        
        if bool_var == True: 
            result += YELLOW_BOX
        else: 
            result += WHITE_BOX

    idx += 1

print(result)


# Part 1
if guess != secret_word: 
    print("Not quite. Play again soon!")
else: 
    print("Woo! You got it!")