# inplace optimised merge sort


# main function
def merge_sort(lis):
    # base condition
    if len(lis) <= 1:
        return lis
    # calculating the mid index
    mid = len(lis) // 2
    # dividing the list in two parts & recursively calling merge_sort function on both of them
    list_1 = merge_sort(lis[:mid])
    list_2 = merge_sort(lis[mid:])
    # calling merge function on the sub lists and returning the result to the previous stage
    return merge(list_1, list_2)


# inplace merge function
def merge(lis1, lis2):
    # pointer for lis1 starting from index 0
    i = 0
    # while i points till the end of lis1
    while i < len(lis1):  # this step will consume O(n/2) i.e O(n) time
        # condition to check the ith element of lis1 is lesser than oe equals to the 0th element of lis 2
        if lis1[i] <= lis2[0]:
            # incrementing the pointer value to point to the next element of lis1
            i += 1
        # condition to check if the ith element of lis1 is greater than the 0th element of lis 2
        else:
            # to swap slice of lis1 starting from the ith index and lis2
            lis1[i:], lis2 = lis2, lis1[i:]   # this step the slice operation will consume O(n -1), O(n -2), O(n -3)... O(1) time i.e O(n)
    # returning the combined lists
    return lis1 + lis2


print(merge_sort([6, 8, 4, 9, 2, 3, 7]))

# ------------------------------ explanation -----------------------------------

# input
# 6 8 4 9 2 3 7

# output
# 2 3 4 6 7 8 9

# execution
# [6 8 4 9 2 3 7]    -------------------------    input
# [6 8 4] - [9 2 3 7]    ---------------------    splitting in stage - 1
# [6] = [8 4] - [9 2] = [3 7]    -------------    splitting in stage - 2
# [6] = [8] . [4] - [9] . [2] = [3] . [7]    -    splitting in stage - 3
# [6] = [4 8] - [2 9] = [3 7]    -------------    rearranging, merging result of stage -3 for stage - 2
# [4 6 8] - [2 3 7 9]    ---------------------    rearranging, merging result of stage -2 for stage - 1
# [2 3 4 6 7 8 9]    -------------------------    output


# explanation for merge function with lis1 = [4, 6, 8] and lis2 = [2, 3, 7, 9]

# lis1 = [4, 6, 8]      lis2 = [2, 3, 7, 9]         -----       input to the merge function
#         i=0

# lis1 = [2, 3, 7, 9]      lis2 = [4, 6, 8]         -----       first pass else condition executes
#         i=0

# lis1 = [2, 3, 7, 9]      lis2 = [4, 6, 8]         -----       second pass if condition executes
#            i=1

# lis1 = [2, 3, 7, 9]      lis2 = [4, 6, 8]         -----       third pass if condition executes
#               i=2

# lis1 = [2, 3, 4, 6, 8]      lis2 = [7, 9]         -----       fourth pass else condition executes
#               i=2

# lis1 = [2, 3, 4, 6, 8]      lis2 = [7, 9]         -----       fifth pass if condition executes
#                  i=3

# lis1 = [2, 3, 4, 6, 8]      lis2 = [7, 9]         -----       sixth pass if condition executes
#                     i=4

# lis1 = [2, 3, 4, 6, 7, 9]      lis2 = [8]         -----       seventh pass else condition executes
#                     i=4

# lis1 = [2, 3, 4, 6, 7, 9]      lis2 = [8]         -----       eight pass if condition executes
#                        i=5

# lis1 = [2, 3, 4, 6, 7, 8]      lis2 = [9]         -----       ninth pass else condition executes
#                        i=5

# lis1 = [2, 3, 4, 6, 7, 8]      lis2 = [9]         -----       tenth pass if condition executes
# i=6

# loop exits as value of i is no more less than the length of lis1
# merge function returns [2, 3, 4, 6, 7, 8] + [9] i.e [2, 3, 4, 6, 7, 8, 9] to merge_sort function
