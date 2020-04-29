def findMin_Max(lis):
    min_elem, max_elem = lis[0], lis[0]
    for i in lis:
        if i < min_elem:
            min_elem = i
        elif i > max_elem:
            max_elem = i
    return min_elem, max_elem


# Solution 1 (not stable)
def countingSort(arr):
    min_elem, max_elem = findMin_Max(arr)
    # count_arr = [0 for i in range(max_elem - min_elem)]
    count_arr = [0] * (max_elem - min_elem + 1)
    for i in arr:
        count_arr[i - min_elem] += 1
    result = []
    for j in range(len(count_arr)):
        for k in range(count_arr[j]):
            result.append(j + min_elem)
    return result


# Solution 2 (not stable)
def countingSort(arr):
    # print(arr)
    min_elem, max_elem = findMin_Max(arr)
    # count_arr = [0 for i in range(max_elem - min_elem)]
    count_arr = [0] * (max_elem - min_elem + 1)
    for i in arr:
        count_arr[i - min_elem] += 1
    # print('Count array', count_arr)
    result = [0] * len(arr)
    for z in range(1, len(count_arr)):
        count_arr[z] = count_arr[z - 1] + count_arr[z]
    # print('Cumulative count array', count_arr)
    for m in range(len(arr)):
        count_arr[arr[m] - min_elem] -= 1
        result[count_arr[arr[m] - min_elem]] = arr[m]
    return result


# Solution 3 (stable)
def countingSort(arr):
    # print(arr)
    min_elem, max_elem = findMin_Max(arr)
    # count_arr = [0 for i in range(max_elem - min_elem)]
    count_arr = [0] * (max_elem - min_elem + 1)
    for i in arr:
        count_arr[i - min_elem] += 1
    # print('Count array', count_arr)
    result = [0] * len(arr)
    for z in range(1, len(count_arr)):
        count_arr[z] = count_arr[z - 1] + count_arr[z]
    # print('Cumulative count array', count_arr)
    for m in range(len(arr) - 1, -1, -1):
        count_arr[arr[m] - min_elem] -= 1
        result[count_arr[arr[m] - min_elem]] = arr[m]
    return result


print(countingSort(
    [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76,
     85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78,
     24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16,
     82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33]))

# print('result : ', countingSort(
#     [5, 3, 5, 3, 4, 3, 2, 4]))


# -------------------------------------------------------------------------------------------------------------------------

# Output : The student's grade is : [1, 1, 3, 3, 6, 8, 9, 9, 10, 12, 13, 16, 16, 18, 20, 21, 21, 22, 23, 24, 25, 25,
# 25, 27, 27, 30, 30, 32, 32, 32, 33, 33, 33, 34, 39, 39, 40, 40, 41, 42, 43, 44, 44, 46, 46, 48, 50, 53, 56, 56, 57,
# 59, 60, 61, 63, 65, 67, 67, 68, 69, 69, 69, 70, 70, 73, 73, 74, 75, 75, 76, 78, 78, 79, 79, 80, 81, 81, 82, 83, 83,
# 84, 85, 86, 86, 87, 87, 89, 89, 89, 90, 90, 91, 92, 94, 95, 96, 98, 98, 99, 99]
