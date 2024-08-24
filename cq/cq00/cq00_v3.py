def get_ones_place(inp_num):
    return str(inp_num)[1]

def get_tenths_place(inp_num):
    return str(inp_num)[0]

def digit_at_positions(inp_num: int): 
    print("The number in the tenths place is " + get_tenths_place(inp_num) + ", and the number in the ones place is, " + get_ones_place(inp_num) + ".")


# Example usage:
digit_at_positions(45)  # Should print "The number in the tenths place is 4, and the number in the ones place is 5"
digit_at_positions(89) 