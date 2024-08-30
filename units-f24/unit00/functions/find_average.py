def sum(first_num, sec_num, third_num): 
    return first_num + sec_num + third_num


def find_average(first_num, sec_num, third_num):
    return sum(first_num=first_num, sec_num=sec_num, third_num=third_num) / len(str(first_num)[0] + str(sec_num)[0] + str(third_num)[0])
    
# Example usage:
print(find_average(first_num=1, sec_num=20, third_num=30))
