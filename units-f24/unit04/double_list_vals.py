def double_elements(inp_list, index=0):
    if index < len(inp_list):
        inp_list[index] *= 2  # Mutate the current element
        double_elements(inp_list, index + 1)  # Recursively call the function for the next element

# Example usage
my_list = [1, 2, 3, 4, 5]
double_elements(my_list)
print(my_list)  # Output: [2, 4, 6, 8, 10]
