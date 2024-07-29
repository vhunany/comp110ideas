"""
Challenge Question
topics:
    - functions
    - lists
    - iterating through lists
    - modifying list items
    - printing out lists
"""


def remove_repeats(inp_list: list[int]) -> None:
    """Mutates inp_list to remove any repeating numbers."""
    idx: int = 0
    while idx < len(inp_list):  # iterate through the list
        # iterate through each number and compare
        comparing_num: int = inp_list[idx]
        iter_idx: int = idx + 1  # to avoid looping over the same zeroth idx
        while iter_idx < len(inp_list):
            if comparing_num == inp_list[iter_idx]:
                inp_list.pop(iter_idx)  # pop decreases the size of the inp_list and indices are changed
            else:
                iter_idx += 1  # pop already allows for iteration so don't increase idx or you will jump over an index
        idx += 1


# example
remove_repeats([4, 8, 9, 4, 2, 2, 0, 9, 7, 10])

# [4, 8, 9, 2, 0, 7, 10]


def insert(list: list[int], num_to_insert: int) -> None:
    list.append(num_to_insert)
    bubble_up_sort(list)


def bubble_up_sort(list: list[int]) -> None:
    second_to_last_idx: int = len(list) - 2
    last_idx: int = len(list) - 1
    while last_idx > 0: 
        val_sec_to_last: int = list[second_to_last_idx]
        val_last: int = list[last_idx]
        if list[second_to_last_idx] > list[last_idx]:
            # swap
            list[last_idx] = val_sec_to_last
            list[second_to_last_idx] = val_last

        last_idx -= 1
        second_to_last_idx -= 1


# example
a: list[int] = []
insert(a, 10)
insert(a, 19)
insert(a, 5)
insert(a, 2)
insert(a, 1)
insert(a, 0)
insert(a, 14)
insert(a, -4)
insert(a, 9)
print(a)  # expected [-4, 0, 1, 2, 5, 9, 10, 14, 19]

# ^ select and then shift + return and it will import in the repl
