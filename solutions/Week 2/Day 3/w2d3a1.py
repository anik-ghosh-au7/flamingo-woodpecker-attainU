# Solution 1


def sort_dict(dict_):
    return dict(sorted(dict_.items(), key=lambda i: i[1]))


def rev_sort_dict(dict_):
    return dict(sorted(dict_.items(), key=lambda i: i[1], reverse=True))


print(sort_dict({'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}))
print(rev_sort_dict({'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}))


# Solution 2

# Using zip method to combine the keys and values of the dictionary, output is a series of tuples
# ('one', 1) ('three', 3) ('five', 5) ('two', 2) ('four', 4)


def sort_dict(dict_):
    return dict(sorted(zip(dict_.keys(), dict_.values()), key=lambda i: i[1]))


def rev_sort_dict(dict_):
    return dict(sorted(zip(dict_.keys(), dict_.values()), key=lambda i: i[1], reverse=True))


print(sort_dict({'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}))
print(rev_sort_dict({'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}))


# -------------------------------------------------------------------------------------------------------------------------


# Output :

# {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
# {'five': 5, 'four': 4, 'three': 3, 'two': 2, 'one': 1}
