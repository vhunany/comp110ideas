def sum_of_digits(n):
    # Base case: when n is 0
    if n == 0:
        return 0
    else:
        # Last digit: n % 10
        # Rest of the number: n // 10
        return (n % 10) + sum_of_digits(n // 10)

# Example usage
print(sum_of_digits(123))  # Output: 6 (1 + 2 + 3)
print(sum_of_digits(4567)) # Output: 22 (4 + 5 + 6 + 7)
print(sum_of_digits(0))    # Output: 0
print(sum_of_digits(9))    # Output: 9
