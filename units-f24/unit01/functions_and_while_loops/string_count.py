def count_characters(s):
    index = 0
    counter = 0
    while index < len(s):
        if s[index] != ' ':
            counter += 1
        index += 1
    return counter

def analyze_string(s):
    char_count = count_characters(s)
    if char_count > 10:
        return "The string is long and has " + str(char_count) + " characters (excluding spaces)."
    else:
        return "The string is short and has " + str(char_count) + " characters (excluding spaces)."

test_string = "Hello, how are you doing today?"
result = analyze_string(test_string)
print(result)