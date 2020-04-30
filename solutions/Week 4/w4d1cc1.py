# def coin_change(to_return, coins):
#     coins.sort()
#     flag = None
#     for c in coins:
#         if c == to_return:
#             # print("c--> ",c)
#             return c
#         elif c < to_return:
#             flag = c
#             # print("flag-->", flag)
#     temp_balance = to_return - flag
#     # print("temp balance-->", temp_balance)
#     result = [flag] + [coin_change(temp_balance, coins)]
#     return flatten(result, [])
#
#
# def flatten(lis, output):
#     for i in lis:
#         if type(i) == list:
#             flatten(i, output)
#         else:
#             output.append(i)
#     return output
#
#
# print(coin_change(28, [1, 10, 5, 2]))


# minimum no. of coins required to change to_return

# def return_change(to_return, coins):
#     coins.sort()
#     return coin_change(to_return, coins)
#
#
# def coin_change(to_return, coins):
#     flag = None
#     for c in coins:
#         if c == to_return:
#             # print("c-->",c)
#             return [c]
#         elif c < to_return:
#             flag = c
#             # print("flag-->", flag)
#     temp_balance = to_return - flag
#     # print("temp balance-->", temp_balance)
#     result = [flag] + coin_change(temp_balance, coins)
#     return result
#
#
# print(return_change(28, [1, 10, 5, 2]))  # [10, 10, 5, 2]
# print(return_change(10, [5, 3, 2]))  # [5, 5]
# print(return_change(53, [4, 5, 6]))  # [6, 6, 6, 6, 6, 6, 6, 6, 5]

# total number of unique ways to return coins for to_return

# def coin_change(to_return, coins):
#     if to_return < 0 or len(coins) == 0:
#         return 0
#     if to_return == 0:
#         return 1
#     return coin_change(to_return, coins[1:]) + coin_change(to_return - coins[0], coins)
#
#
# print(coin_change(10, [3, 5, 2]))

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


# to get all possible combinations of the total number of ways to return coins for to_return


def coinchange(amt, coin1, coin2, coin3):
    if amt < 0:
        return 0
    elif amt == 0:
        return 1
    return coinchange(amt - coin1, coin1, coin2, coin3) + coinchange(amt - coin2, coin1, coin2, coin3) + coinchange(amt - coin3, coin1, coin2, coin3)


print(coinchange(10, 3, 5, 2))
