def count_digits(text):
    index = 0
    digit_count = 0
    digits = "0123456789"
    
    while index < len(text):
        char = text[index]
        is_digit = False
        
        # Check if char is in the string of digits
        digit_index = 0
        while digit_index < len(digits):
            if char == digits[digit_index]:
                is_digit = True
            digit_index += 1
        
        if is_digit:
            digit_count += 1
        
        index += 1
    
    return digit_count

text = "abc123def456ghi789"
result = count_digits(text)
print(result)
