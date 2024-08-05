def num_instances(inp_str: str, search_str: str):
    """Counts the number of instances of a 'search_str' in an inp_str."""
    count = 0  # To count occurrences of search_str
    index = 0  # To iterate through inp_str

    while index <= len(inp_str) - len(search_str):
        # Check if the substring of inp_str starting at index matches search_str
        match = True
        sub_index = 0
        
        while sub_index < len(search_str):
            if inp_str[index + sub_index] != search_str[sub_index]:
                match = False
            sub_index += 1
        
        if match:
            count += 1
            index += len(search_str)  # Move index by length of search_str to avoid overlapping matches
        else:
            index += 1  # Move to the next character in inp_str

    print(count)

# Example usage
num_instances("MarryyyHeLloMaoy", "Marryy")  # Output should be 1
num_instances("HelloHelloHEllo", "el")  # Output should be 2