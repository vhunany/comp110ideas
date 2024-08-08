def count_num_of_appearances(inp_list: list[int] | list[str]) -> dict[int, int] | dict[int, str]:
    counts: dict[int, int] | dict[int, str] = {}
    for val in inp_list:
        if val in counts:
            counts[val] += 1
        else:
            counts[val] = 1
    return counts

numbers: list[int] = [1, 1, 0]
print(count_num_of_appearances(numbers))  # Output: {1: 2, 0: 1}
print(count_num_of_appearances(["the", "funny", "monkey"]))  # Output: {'the': 1, 'funny': 1, 'monkey': 1}
print(count_num_of_appearances(["funny", "funny", "monkey"]))    # Output: {'funny': 2, 'monkey': 1}

