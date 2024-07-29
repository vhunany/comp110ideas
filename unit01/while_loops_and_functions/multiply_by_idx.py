def multiply_by_each_idx(number: int) -> str:
    """
    For an input number, each digit within the inp_number is multiplied by it's index value.
    This new number is stored and returned. 
    """
    # Convert the number to a string to process each digit
    num_str = str(number)
    
    # Initialize an empty string to build the result
    result = ""
    
    # Iterate through each digit and its index
    index = 0
    while index < len(num_str):
        # Get the digit at the current index
        digit = int(num_str[index])
        
        # Multiply the digit by its index and append to result
        result += str(digit * index)
        
        # Move to the next index
        index += 1
    
    return result

# Example usage
print(multiply_by_each_idx(10784))  # Output should be "00142416"