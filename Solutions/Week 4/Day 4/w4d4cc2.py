# merge sort without using recursion


def merge_sort(arr):
    result = []
    for i in range(len(arr)):
        # print("merging ", [arr[i]], " and ", result)
        result = merge([arr[i]], result)
        # print("at i = ", i, " result = ", result)
    return result


def merge(list_1, list_2):
    result = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1
    result += list_1[i:]
    result += list_2[j:]
    return result


print(merge_sort([8, 6, 9, 4, 2, 3, 7]))


# ------------------------------- explanation ----------------------------------

# input
# 8 6 9 4 2 3 7

# output
# 2 3 4 6 7 8 9

# explanation
# merging  [8]  and  []
# at i =  0  result =  [8]
# merging  [6]  and  [8]
# at i =  1  result =  [6, 8]
# merging  [9]  and  [6, 8]
# at i =  2  result =  [6, 8, 9]
# merging  [4]  and  [6, 8, 9]
# at i =  3  result =  [4, 6, 8, 9]
# merging  [2]  and  [4, 6, 8, 9]
# at i =  4  result =  [2, 4, 6, 8, 9]
# merging  [3]  and  [2, 4, 6, 8, 9]
# at i =  5  result =  [2, 3, 4, 6, 8, 9]
# merging  [7]  and  [2, 3, 4, 6, 8, 9]
# at i =  6  result =  [2, 3, 4, 6, 7, 8, 9]
