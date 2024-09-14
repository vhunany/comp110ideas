def get_starting_point(word: str) -> int:
    return int(len(word) / 3)

def shift_position(index: int) -> int:
    return index - 1

def extract_character(word: str, index: int) -> str:
    return word[index]

def main(word: str) -> None:
    print("The hidden character is: " + extract_character(word=word, index=shift_position(index=get_starting_point(word=word))))

main(word="mystery")


# def flavor(taste: str, percent: float) -> None:
#     print("This flavor is " + str(percent) + "% " + taste)

# flavor(taste="umami", percent=100)

# def have_done(task, completed) -> str:
#     return "Completed " + task + ": " + str(completed)

# print(have_done(task="homework", completed=False))


