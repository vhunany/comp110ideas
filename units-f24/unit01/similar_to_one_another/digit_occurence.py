def count_digit_occurrences(text, digit):
    index = 0
    digit_count = 0
    
    while index < len(text):
        char = text[index]
        is_digit = False
        
        # Check if char is the digit we are looking for
        digit_index = 0
        while digit_index < len(digit):
            if char == digit[digit_index]:
                is_digit = True
            digit_index += 1
        
        if is_digit:
            digit_count += 1
        
        index += 1
    
    return digit_count

text = "123453123456789123"
digit = "3"
result = count_digit_occurrences(text, digit)
print(result)
