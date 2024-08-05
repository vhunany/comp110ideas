def rotate(inp_list, rot_num):
    if rot_num <= 0:
        return

    # Create a new list to build the rotated result
    rotated_list = []
    
    # Rotate the list by popping elements from the end and appending to the new list
    for num in range(0, len(inp_list)):
        rotated_list.append(inp_list.pop(0))  # Remove the first element and append it to the new list
    
    # Move the last k elements to the beginning
    for num in range(0, rot_num):
        inp_list.append(rotated_list.pop(0))  # Move elements from the rotated list back to the original list

def rotate_list(inp_list, rot_num):
    if inp_list:
        rot_num = rot_num % len(inp_list)  # Normalize rot_num to be within the length of the list
        rotate(inp_list, rot_num)

# Example usage
my_list = [1, 2, 3, 4, 5]
rotate_list(my_list, 2)
print(my_list)  # Output: [4, 5, 1, 2, 3]

my_second_list = [10, 20, 30, 40, 50]
rotate_list(my_second_list, 7)
print(my_second_list)  # Output: [40, 50, 10, 20, 30]

my_third_list = [1, 2, 3, 4]
rotate_list(my_third_list, 0)
print(my_third_list)  # Output: [1, 2, 3, 4]