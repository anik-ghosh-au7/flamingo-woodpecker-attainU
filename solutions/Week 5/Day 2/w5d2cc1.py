# https://practice.geeksforgeeks.org/problems/inversion-of-array/0

# input
# 1
# 5
# 2 4 1 3 5

# output
# 3

# input
# 1
# 5
# 5 4 3 2 1

# output
# 19

#code
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
