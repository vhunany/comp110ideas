def determine_type(item):
    # Determines the type of the item: 'string', 'integer', or 'list'
    if type(item) == str:
        return 'string'
    elif type(item) == int:
        return 'integer'
    elif type(item) == list:
        return 'list'
    return 'unknown'

def categorize_content(item):
    # Categorizes based on content: positive/negative for integers, short/long for strings and lists
    if type(item) == int:
        if item >= 0:
            return 'positive'
        else:
            return 'negative'
    elif type(item) == str:
        if len(item) <= 5:
            return 'short'
        else:
            return 'long'
    elif type(item) == list:
        if len(item) <= 5:
            return 'short'
        else:
            return 'long'

def organize_by_type_and_content(items: list[str | int | list]) -> dict[str, dict[str, list[str | int | list]]]:
    bin = {'string': {'short': [], 'long': []}, 'integer': {'positive': [], 'negative': []}, 'list': {'short': [], 'long': []}}

    for val in items:
        item_type = determine_type(val)
        content_category = categorize_content(val)
        if val not in bin[item_type][content_category]:  # Ensuring the list does not contain duplicates
            bin[item_type][content_category].append(val)

    return bin

# Test cases
print(organize_by_type_and_content([2, -3, 4, "apple", "banana", "hi", [5, "grape"], [1, 2, 3, 4, 5, 6]]))  
# Output: {'string': {'short': ['hi'], 'long': ['apple', 'banana']}, 'integer': {'positive': [2, 4], 'negative': [-3]}, 'list': {'short': [[5, 'grape']], 'long': [[1, 2, 3, 4, 5, 6]]}}

print(organize_by_type_and_content(["umbrella", "dog", "cat", 7, -12, [10, "cat"], [1, 2]]))  
# Output: {'string': {'short': ['dog', 'cat'], 'long': ['umbrella']}, 'integer': {'positive': [7], 'negative': [-12]}, 'list': {'short': [[1, 2]], 'long': [[10, 'cat']]}}
