# Solution


def hourglassSum(arr):

    # min value of hourglass sum (max_sum) is when all the 7 elements are -9 = -63

    max_sum = -63

    for i in range(len(arr[0]) - 2):
        for j in range(len(arr[1]) - 2):
            sum_ = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if sum_ > max_sum:
                max_sum = sum_
    return max_sum


# -------------------------------------------------------------------------------------------------------------------------

# calling function and passing the an array as argument
print(hourglassSum([[1, 1, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [1, 1, 1, 0, 0, 0],
                    [0, 0, 2, 4, 4, 0],
                    [0, 0, 0, 2, 0, 0],
                    [0, 0, 1, 2, 4, 0]]))

# Output :
# 19
