def increment_by_position(number: int, position: int) -> int:
    """Returns the input number incremented by its position in the argument list."""
    return number + position

def product_of_positional_increments(num1: int, num2: int, num3: int, num4: int) -> int:
    """Returns the product of numbers incremented by their positions."""
    return (increment_by_position(num1, 0) * increment_by_position(num2, 1) * increment_by_position(num3, 2) * increment_by_position(num4, 3))

# Test the functions
print(product_of_positional_increments(1, 2, 3, 4))