# Solution 1


def create_dict(string):
    result = {}
    for i in range(len(string)):
        if string[i] in result:
            result[string[i]] += 1
        else:
            result[string[i]] = 1
    return result


print(create_dict('w3resource'))


# Solution 2


def create_dict(string):
    result = {}
    for i in string:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result


print(create_dict('w3resource'))


# -------------------------------------------------------------------------------------------------------------------------


# Output :

# {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
