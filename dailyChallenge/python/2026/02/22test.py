def swap_dict_items(test_dict, i, j):
    items = list(test_dict.items())
    items[i], items[j] = items[j], items[i]
    return dict(items)

# Example usage
test_dict = {'Python': 1991, 'Java': 1995, 'C++': 1979, 'JavaScript': 1995}
i, j = 1, 3

print("Original dictionary:", test_dict)
result = swap_dict_items(test_dict, i, j)
print("Swapped dictionary:", result)