def count_vowels(text):
    index = 0
    vowel_count = 0
    vowels = "aeiouAEIOU"
    
    while index < len(text):
        char = text[index]
        is_vowel = False
        
        # Iterate through the string of vowels to check if char is a vowel
        vowel_index = 0
        while vowel_index < len(vowels):
            if char == vowels[vowel_index]:
                is_vowel = True
            vowel_index += 1
        
        if is_vowel:
            vowel_count += 1
        
        index += 1
    
    return vowel_count

text = "This is a sample text with some vowels."
result = count_vowels(text)
print(result)
