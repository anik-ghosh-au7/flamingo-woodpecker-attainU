# https://practice.geeksforgeeks.org/problems/inversion-of-array/0

# input
# 1
# 5
# 2 4 1 3 5

# Explanation
# 2 1 4 3 5 - count = 1
# 2 1 3 4 5 - count = 2
# 1 2 3 4 5 - count = 3

# output
# 3

# input
# 1
# 5
# 5 4 3 2 1

# Explanation
# 4 5 3 2 1 - count = 1
# 4 3 5 2 1 - count = 2
# 4 3 2 5 1 - count = 3
# 4 3 2 1 5 - count = 4

# 3 4 2 1 5 - count = 5
# 3 2 4 1 5 - count = 6
# 3 2 1 4 5 - count = 7

# 2 3 1 4 5 - count = 8
# 2 1 3 4 5 - count = 9

# 1 2 3 4 5 - count = 10

# output
# 10


# Explanation in case of (Merge Sort)

# [2,4,1,3,5]    -------------------------   input
# [2,4] - [1,3,5]    ---------------------   splitting in stage - 1
# [2] = [4] - [1] = [3,5]    -------------   splitting in stage - 2
# [2] = [4] - [1] = [3] . [5]    ---------   splitting in stage - 3
# [2] = [4] - [1] = [3,5]    -------------   rearranging, merging result of stage -3 for stage - 2 count = 0
# [2,4] - [1,3,5]    ---------------------   rearranging, merging result of stage -2 for stage - 1 count = 0
# [1,2,3,4,5]    -------------------------   output count = (2 + 1) = 3


# Explanation in case of (Merge Sort) right list elements are always smaller than the left list while merging
# in this case as the input list is a sorted list in descending order

# [5,4,3,2,1]    -------------------------   input
# [5,4] - [3,2,1]    ---------------------   splitting in stage - 1
# [5] = [4] - [3] = [2,1]    -------------   splitting in stage - 2
# [5] = [4] - [3] = [2] . [1]    ---------   splitting in stage - 3
# [5] = [4] - [3] = [1,2]    -------------   rearranging, merging result of stage -3 for stage - 2 count = 1
# [4,5] - [1,2,3]    ---------------------   rearranging, merging result of stage -2 for stage - 1 count = (1 + (1 + 2)) = 4
# [1,2,3,4,5]    -------------------------   output count = (4 + (2 + 2 + 2)) = 10

# code
t = int(input())
for tt in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    count = [0]


    def merge_sort(lis, count):
        if len(lis) <= 1:
            return lis
        mid = len(lis) // 2
        list_1 = merge_sort(lis[:mid], count)
        list_2 = merge_sort(lis[mid:], count)
        return merge(list_1, list_2, count)


    def merge(list_1, list_2, count):
        result = []
        i = 0
        j = 0
        countme = 0
        while i < len(list_1) and j < len(list_2):
            if list_1[i] <= list_2[j]:
                result.append(list_1[i])
                i += 1
            else:
                result.append(list_2[j])
                j += 1
                countme += len(list_1) - i
        result += list_1[i:]
        result += list_2[j:]
        count[0] += countme
        return result


    merge_sort(arr, count)
    print(count[0])
