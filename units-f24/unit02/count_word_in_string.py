def count_success(log):
    index = 0
    success_count = 0
    word = "SUCCESS"
    word_length = len(word)
    
    while index <= len(log) - word_length:
        match = True
        for i in range(word_length):
            if log[index + i] != word[i]:
                match = False
        
        if match:
            success_count += 1
            index += word_length  # Move index to the end of the "SUCCESS" word
        else:
            index += 1
            
    return success_count

log_text = "INFO: Operation SUCCESS. ERROR: Something went wrong. SUCCESS: Operation completed. INFO: All good. SUCCESS: Another success."
result = count_success(log_text)
print(result)
