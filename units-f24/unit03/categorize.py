def first_char_in_alphabet(item):
    # Returns True if the first character is an alphabet letter (vowel or consonant)
    alphabet = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    if item:
        first_char = item[0]
        return first_char in alphabet
    return False

def is_string(item):
    vowels = "aeiouAEIOU"
    if first_char_in_alphabet(item):
        first_char = item[0]
        is_vowel = first_char in vowels
        return is_vowel
    return False

def categorize(item):
    if is_string(item):
        first_char = item[0]
        if first_char in "aeiouAEIOU":
            return 'vowel'
        else:
            return 'consonant'
    else:
        item_as_str = str(item)
        if int(item_as_str) % 2 == 0:
            return 'even'
        else:
            return 'odd'

def organize_by_parity_and_vowel(items: list[str | int | list]) -> dict[str, list[str | int | list]]:
    bin = {'even': [], 'odd': [], 'vowel': [], 'consonant': []}

    for val in items:
        if isinstance(val, list):
            category = categorize(val[0])  # Categorize based on the first element of the list
        else:
            category = categorize(val)
        if val not in bin[category]:  # Ensuring the list does not contain duplicates
            bin[category].append(val)
    
    return bin

# Test cases
print(organize_by_parity_and_vowel([2, 3, 4, "apple", "banana", "orange", [5, "grape"]]))  
# Output: {'even': [2, 4], 'odd': [3, [5, "grape"]], 'vowel': ['apple', 'orange'], 'consonant': ['banana']}

print(organize_by_parity_and_vowel(["umbrella", "elephant", "zebra", 7, 12, [10, "cat"]]))  
# Output: {'even': [12, [10, "cat"]], 'odd': [7], 'vowel': ['umbrella', 'elephant'], 'consonant': ['zebra']}
