# Solution 1 (Using for loop and in operator)


def combine_dict(dict1, dict2):
    result = {}
    for i in dict1.keys():
        if i in dict2.keys():
            result[i] = dict1[i] + dict2[i]
            del dict2[i]
        else:
            result[i] = dict1[i]
    result.update(dict2)
    return result


print(combine_dict({'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 200, 'd': 400}))


# Solution 2 (Using OR bitwise operator)


def combine_dict(dict1, dict2):
    result = {}
    for key in dict1.keys() | dict2.keys():
        result[key] = dict1.get(key, 0) + dict2.get(key, 0)
    return result


print(combine_dict({'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 200, 'd': 400}))


# Solution 3 (Using Counter)

from collections import Counter


def combine_dict(dict1, dict2):
    return dict(Counter(dict1) + Counter(dict2))


print(combine_dict({'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 200, 'd': 400}))


# Solution 4 (Using .chain() function from itertools and for loop)

import itertools


def combine_dict(dict1, dict2):
    result = {}
    for key, value in itertools.chain(dict1.items(), dict2.items()):
        result[key] = value
    return result


print(combine_dict({'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 200, 'd': 400}))


# Solution 5 (Using .chain() function from itertools)

import itertools


def combine_dict(dict1, dict2):
    return dict(itertools.chain(dict1.items(), dict2.items()))


print(combine_dict({'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 200, 'd': 400}))


# Solution 6 (Using dictionary comprehension and | operator)


def combine_dict(dict1, dict2):
    return {key: dict1.get(key, 0) + dict2.get(key, 0) for key in dict1.keys() | dict2.keys()}


print(combine_dict({'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 200, 'd': 400}))


# Solution 7 (Using dictionary comprehension and | operator and sets)


def combine_dict(dict1, dict2):
    return {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}


print(combine_dict({'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 200, 'd': 400}))


# -------------------------------------------------------------------------------------------------------------------------


# Output :

# {'a': 400, 'b': 400, 'c': 300, 'd': 400}
