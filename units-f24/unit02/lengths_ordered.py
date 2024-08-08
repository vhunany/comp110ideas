def organize_by_length(words: list[str] | list[int]):
    bin = {}
    for val in words:
        if type(val) == int: 
            val = str(val)
            length = len(val)
            if length not in bin:
                bin[length] = []
            if val not in bin[length]:  # Ensuring the list does not contain duplicates
                bin[length].append(int(val))  # repeats but avoids using built in function digit()
        else: 
            length = len(val)
            if length not in bin:
                bin[length] = []
            if val not in bin[length]:  # Ensuring the list does not contain duplicates
                bin[length].append(val)
    return bin

print(organize_by_length(["the", "quick", "fox"]))  # Output: {3: ["the", "fox"], 5: ["quick"]}
print(organize_by_length(["the", "the", "fox"]))    # Output: {3: ["the", "fox"]}
numbers: list[int] = [111, 11, 0, 12]
print(organize_by_length(numbers))  # Output: {3: [111], 2: [11, 12], 1: [0]}