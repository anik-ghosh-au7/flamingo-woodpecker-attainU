# Solution


def dynamicArray(n, queries):
    seqList = [[] for _ in range(n)]
    lastAnswer = 0

    result = []

    for i in range(len(queries)):

        if queries[i][0] == 1:
            x = queries[i][1]
            y = queries[i][2]
            index = (x ^ lastAnswer) % n
            seqList[index].append(y)

        elif queries[i][0] == 2:
            x = queries[i][1]
            y = queries[i][2]
            index = (x ^ lastAnswer) % n
            sub_index = y % len(seqList[index])
            lastAnswer = seqList[index][sub_index]
            result.append(lastAnswer)
            print(sub_index)

    return result

# -------------------------------------------------------------------------------------------------------------------------

# Explanation :

# i :  0

# type 1
# x : 0
# y : 5
# index : 0
# seqList : [[5], []]


# i :  1

# type 1
# x : 1
# y : 7
# index : 1
# seqList : [[5], [7]]


# i :  2

# type 1
# x : 0
# y : 3
# index : 0
# seqList : [[5, 3], [7]]


# i :  3

# type 2
# x : 1
# y : 0
# index : 1
# sub_index : 0
# seqList : [[5, 3], [7]]
# lastAnswer :  7
# result : [7]


# i :  4

# type 2
# x : 1
# y : 1
# index : 0
# sub_index : 1
# list : [[5, 3], [7]]
# lastAnswer : 3
# result : [7, 3]


# -------------------------------------------------------------------------------------------------------------------------

# calling function, passing the an array as argument & printing the result
print(dynamicArray(2, [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]))

# Output :
# [7, 3]
