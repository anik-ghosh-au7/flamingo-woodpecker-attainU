# Binary search using iteration

import time
start_time = time.time()


def iterative_BinarySearch(lis, value):
    low, high = 0, len(lis) - 1
    while low <= high:
        # mid = (high + low) // 2
        mid = high - (high - low) // 2
        if value > lis[mid]:
            low = mid + 1
        elif value < lis[mid]:
            high = mid - 1
        else:
            return mid
    return -1


print(iterative_BinarySearch([2, 6, 8, 9, 13, 16, 28, 35, 49, 56, 83, 97], 49))
print("Time taken by iterative_BinarySearch() is %s seconds" % (start_time-time.time()))


# Binary search using recursion

start_time1 = time.time()


def recursive_BinarySearch(lis, value, count=0):
    if len(lis) == 0:
        return -1
    mid = (len(lis) - 1) // 2
    if lis[mid] == value:
        return mid + count
    elif lis[mid] > value:
        return recursive_BinarySearch(lis[:mid], value, count)
    elif lis[mid] < value:
        count = count + mid + 1
        return recursive_BinarySearch(lis[mid + 1:], value, count)


print(recursive_BinarySearch([2, 6, 8, 9, 13, 16, 28, 35, 49, 56, 83, 97], 49))
print("Time taken by recursive_BinarySearch() is %s seconds" % (start_time1-time.time()))
