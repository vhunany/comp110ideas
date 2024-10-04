def num_instances(phrase, search_char):
    # Initialize count to 0
    count = 0
    
    # Initialize index to 0
    index = 0
    
    # Loop through the phrase using a while loop
    while index < len(phrase):
        # Check if the current character matches the search_char
        if phrase[index] == search_char:
            count += 1
        # Move to the next character
        index += 1
    
    # Return the final count
    return count

print(num_instances('HelloHeLloHEllo', 'e') == 2)
print(num_instances('HelloHelloHello', 'e') == 3)
print(num_instances('Happy Tuesday!', 'y') == 2)
print(num_instances('Happy Tuesday!', 'z') == 0)

print(num_instances('a', 'a') == 1)
print(num_instances('a', 'b') == 0)
print(num_instances('abcabcabc', 'a') == 3)
print(num_instances('This is an example sentence.', 'e') == 5)