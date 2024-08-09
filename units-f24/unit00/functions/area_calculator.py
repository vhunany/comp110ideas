def calculate_area(width: float, length: float) -> float:
    """Calculate the area of a rectangle given its width and length."""
    return width * length

def maximize_area(width: float, length: float, multiply_by: float) -> float:
    """Maximize the area by multiplying the width and length by a specified factor."""
    return calculate_area(width=width * multiply_by, length=length * multiply_by)

def minimize_area(width: float, length: float, multiply_by: float) -> float:
    """Minimize the area by multiplying the width and length by a specified factor."""
    return calculate_area(width=width * multiply_by, length=length * multiply_by)

def main():
    """Main program to calculate the original, maximized, and minimized areas of a rectangle."""
    original_width: float = 5.0
    original_length: float = 10.0
    maximize_factor: float = 1.5
    minimize_factor: float = 0.5
    
    print(f"Original area: {calculate_area(width=original_width, length=original_length)}")
    print(f"Maximized area: {maximize_area(width=original_width, length=original_length, multiply_by=maximize_factor)}")
    print(f"Minimized area: {minimize_area(width=original_width, length=original_length, multiply_by=minimize_factor)}")


main()

"""A cozy embrace."""

def hug(it: str)-> str:
    """Surround it."""
    return suffix(word = prefix(word = it, pre =" -("), post =")-")

def suffix(word: str, post: str) -> str:
    """After ... """
    return word + post

def prefix(word: str, pre: str ) -> str:
    """Before ... """
    return pre + word


print (hug( it =" turtle "))