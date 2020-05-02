# recursive solution

def powerSum(X, N, n=1):
    if n**N > X:
        return 0
    elif n**N == X:
        return 1
    return powerSum(X, N, n+1) + powerSum(X-n**N, N, n+1)


print(powerSum(10, 2))


# ----------------------  explanation  -----------------------------


#                          (10,2,1)  -------------------  Input
#                         /        \
#                        /          \
#                   (10,2,2)        (9,2,2)  -----------  Step 1
#                   /     \         /     \
#                  /       \       /       \
#               (10,2,3) (6,2,3) (9,2,3) (5,2,3)  ------  Step 2
#                /     \      |     |       |
#               /       \     |     |       |
#           (10,2,4) (1,2,4)  |     |       |     ------  Step 3
#               |       |     |     |       |
#               0       0     0     1       0     ------  Output (Summation of return values)


# alternate solution


# def powerSum(X, N, n=1):
#     count = 0
#     for i in range(n, X):
#         ans = X-i**N
#         if ans == 0:
#             count += 1
#         if ans > 0:
#             count += powerSum(ans, N, i+1)
#         continue
#     return count


# print(powerSum(10, 2))
