# input
# [70, 50, 30, 10, 20, 40, 60]

# output
# [10, 20, 30, 40, 50, 60, 70]

# explanation
# [70,50,30,10,20,40,60]    -------------------------   input
# [70,50,30] - [10,20,40,60]    ---------------------   splitting in stage - 1
# [70] = [50,30] - [10,20] = [40,60]    -------------   splitting in stage - 2
# [70] = [50] . [30] - [10] . [20] = [40] . [60]    -   splitting in stage - 3
# [70] = [30,50] - [10,20] = [40,60]    -------------   rearranging, merging result of stage -3 for stage - 2
# [30,50,70] - [10,20,40,60]    ---------------------   rearranging, merging result of stage -2 for stage - 1
# [10,20,30,40,50,60,70]    -------------------------   output


# merge sort
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


# merging function
def merge(list_1, list_2):
    result = []
    i = 0
    j = 0
    # this loop will run till the ith el or the jth el is the last element of their respective lists
    while i < len(list_1) and j < len(list_2):
        # condition to check the ith el of ls1 with jth el ls2 and append the smaller to result
        if list_1[i] <= list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1
    # will add the left over elements of either list
    result += list_1[i:]
    result += list_2[j:]
    # returning the result list to the merge_sort function
    return result


input_list = [70, 50, 30, 10, 20, 40, 60]
print(merge_sort(input_list))