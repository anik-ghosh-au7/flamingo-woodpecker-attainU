# Solution 1 (Using basic for loop)


def generate_dict(num):
    result = {}
    for i in range(1, num + 1):
        result[i] = i * i
    return result


print(generate_dict(10))


# Solution 2 (Using dictionary comprehension)


def generate_dict(num):
    return {x: x * x for x in range(1, num + 1)}


print(generate_dict(10))


# Solution 3 (Using map, lambda function & list comprehension)


def generate_dict(num):
    return dict(map(lambda v: (v, v * v), [_ for _ in range(1, num + 1)]))


print(generate_dict(10))

# -------------------------------------------------------------------------------------------------------------------------


# Output :

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
