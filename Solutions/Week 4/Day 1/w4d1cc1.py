# total number of unique ways to return coins for to_return

# def coin_change(to_return, coins):
#     if to_return < 0 or len(coins) == 0:
#         return 0
#     if to_return == 0:
#         return 1
#     return coin_change(to_return, coins[1:]) + coin_change(to_return - coins[0], coins)
#
#
# print(coin_change(10, [3, 5, 2]))  # 4


# ------------------ explanation -------------------------

# Recursive tree

#                            10, [3, 5, 2]  ----------------------------------------------------  Input
#                            /            \
#                           /              \
#                 10, [5, 2]                7, [3, 5, 2]  --------------------------------------  Step 1
#                /          \               /          \
#               /            \             /            \
#         10, [2]        5, [5, 2]       7, [5, 2]       4, [3, 5, 2]  -------------------------  Step 2
#        /       \         /     \        /     \               /    \
#       /         \       /       \      /       \             /      \
# 10, [_]      8, [2]  5, [2]  0, [5,2] 7, [5]  2, [5, 2]    4,[5,2]   1,[3,5,2]  --------------  Step 3
#    |        / \       /  \      |    / \        /  \          /  \        /   \
#    |       /   \     /    \     |   /   \      /    \        /    \      /     \
#    |  8,[_]6,[2]  5,[_] 3,[2]   | 7,[_] 2,[5] 2,[2] -3[5,2]4,[2] -1[5,2]1,[5,2] -2[3,5,2]  ---  Step 4
#    |    |    / \     |    / \   |   |    / \     / \    |    / \      |      / \       |
#    |    |   /   \    |   /   \  |   |   /   \   /   \   |   /   \     |     /   \      |
#    |    |6[_]  4[2]  |3[_] -1[2]|   |2[_] -3[5]2[_]0[2] | 4[_] 2[2]   |  1,[2] -3[5,2] |   ---  Step 5
#    |    | |     /\   |  |    |  |   |  |    |   |   |   |   |   /\    |   /\     |     |
#    |    | |    /  \  |  |    |  |   |  |    |   |   |   |   |  /  \   |  /  \    |     |
#    |    | | 4[] 2[2] |  |    |  |   |  |    |   |   |   |   | 2[] 0[2]|1[] -1[2] |     |   ---  Step 6
#    |    | |  |  /\   |  |    |  |   |  |    |   |   |   |   |  |   |  | |   |    |     |
#    |    | |  | /  \  |  |    |  |   |  |    |   |   |   |   |  |   |  | |   |    |     |
#    |    | |  |2[]0[2]|  |    |  |   |  |    |   |   |   |   |  |   |  | |   |    |     |   ---  Step 7
#    |    | |  | |   | |  |    |  |   |  |    |   |   |   |   |  |   |  | |   |    |     |
#    0    0 0  0 0   1 0  0    0  1   0  0    0   0   1   0   0  0   1  0 0   0    0     0   ---  Output (Summation of return values)


# to get all possible permutations of the total number of ways to return coins for to_return


def coinchange(to_return, lis):
    if to_return < 0:
        return 0
    elif to_return == 0:
        return 1
    return coinchange(to_return - lis[0], lis) + coinchange(to_return - lis[1], lis) + coinchange(to_return - lis[2], lis)


print(coinchange(10, [3, 5, 2]))  # 14
