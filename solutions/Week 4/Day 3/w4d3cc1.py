a = [10, 12, 13, 14, 18, None, None, None, None, None]
b = [16, 17, 19, 20, 22]


def merge(arr1, arr2):
    i, k, j = len(arr1) - 1, len(arr1) - 1, len(arr2) - 1
    while arr1[i] is None:
        i -= 1
    # print(i, k, j)  # 4 9 4
    while i >= 0 and j >= 0:
        if arr2[j] > arr1[i]:
            arr1[k] = arr2[j]
            k -= 1
            j -= 1
        else:
            arr1[k] = arr1[i]
            k -= 1
            i -= 1
    return arr1


print(merge(a, b))  # [10, 12, 13, 14, 16, 17, 18, 19, 20, 22]


# -------------------------- explanation -----------------------------------


# Start

# arr1 = [10, 12, 13, 14, 18, None, None, None, None, None]
#                         i=4                          k=9

# arr2 = [16, 17, 19, 20, 22]
#                         j=4


# First Pass

# goes inside if condition as arr2[j] > arr1[i]

# arr1 = [10, 12, 13, 14, 18, None, None, None, None, 22]
#                         i=4                    k=8

# arr2 = [16, 17, 19, 20, 22]
#                     j=3


# Second Pass

# goes inside if condition as arr2[j] > arr1[i]

# arr1 = [10, 12, 13, 14, 18, None, None, None, 20, 22]
#                         i=4              k=7

# arr2 = [16, 17, 19, 20, 22]
#                 j=2


# Third Pass

# goes inside if condition as arr2[j] > arr1[i]

# arr1 = [10, 12, 13, 14, 18, None, None, 19, 20, 22]
#                         i=4        k=6

# arr2 = [16, 17, 19, 20, 22]
#             j=1


# Fourth Pass

# goes inside else condition as arr2[j] < arr1[i]

# arr1 = [10, 12, 13, 14, 18, None, 18, 19, 20, 22]
#                     i=3      k=5

# arr2 = [16, 17, 19, 20, 22]
#             j=1


# Fifth Pass

# goes inside if condition as arr2[j] > arr1[i]

# arr1 = [10, 12, 13, 14, 18, 17, 18, 19, 20, 22]
#                     i=3 k=4

# arr2 = [16, 17, 19, 20, 22]
#         j=0


# Sixth Pass

# goes inside if condition as arr2[j] > arr1[i]

# arr1 = [10, 12, 13, 14, 16, 17, 18, 19, 20, 22]
#                    i,k=3

# arr2 = [16, 17, 19, 20, 22]
# j=-1


# while loop exits as value of j becomes less than 0
# function returns arr1


