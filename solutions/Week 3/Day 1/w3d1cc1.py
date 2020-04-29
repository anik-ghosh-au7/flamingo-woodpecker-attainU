#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the icecreamParlor function below.

# O(n^2) Solution
# def icecreamParlor(m, arr):
#     length = len(arr)
#     for i in range(length):
#         for j in range(i + 1, length):
#             if arr[i] + arr[j] == m:
#                 return [i + 1, j + 1]


# O(nlogn) Solution
def icecreamParlor(m, arr):
    hash_list = sorted(enumerate(arr), key=lambda v: v[1])
    i, j = 0, len(hash_list) - 1
    while i < j:
        if hash_list[i][1] + hash_list[j][1] > m:
            j -= 1
        elif hash_list[i][1] + hash_list[j][1] < m:
            i += 1
        else:
            return sorted([hash_list[i][0] + 1, hash_list[j][0] + 1])


# print(*icecreamParlor(4, [1, 4, 5, 3, 2]))
# print(*icecreamParlor(4, [2, 2, 4, 3]))
# print(*icecreamParlor(6, [1, 3, 4, 6, 5]))
# print(*icecreamParlor(6, [1, 3, 4, 5, 6]))

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        print(' '.join(map(str, result)))
        print('\n')


# -------------------------------------------------------------------------------------------------------------------------

# Input part 1 :
# 2
# 4
# 5
# 1 4 5 3 2

# Output part 1 :
# 1 4


# Input part 2 :
# 4
# 4
# 2 2 4 3

# Output part 2 :
# 1 2
