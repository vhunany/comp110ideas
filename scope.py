def count_digits(input_string):
    # Local variable to track the digit we're currently counting
    current_digit = 0
    
    while current_digit < 10:  # Loop over digits from 0 to 9
        count = 0
        idx = 0
        
        while idx < len(input_string):
            if input_string[idx] == str(current_digit):
                count += 1
            idx += 1
        
        update_global_result(f"({current_digit}, {count})")
        
        current_digit += 1

def update_global_result(new_entry):
    # Function to update the global string result
    global global_result
    global_result += new_entry + " "  # Concatenate the new entry with a space

global_result = ""
input_string = "134562341"
count_digits(input_string)
print(global_result)