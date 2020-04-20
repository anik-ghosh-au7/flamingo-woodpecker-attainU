from functools import reduce

lis = [1, 5, 4, 9, 8]

max_elme = reduce(lambda a, b: a if a > b else b, lis)
min_elme = reduce(lambda a, b: a if a < b else b, lis)

print(max_elme)
print(min_elme)
