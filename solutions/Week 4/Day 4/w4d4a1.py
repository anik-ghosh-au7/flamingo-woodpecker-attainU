def closestNumbers(arr):
    arr.sort()
    min_diff = arr[1] - arr[0]
    result = []

    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] < min_diff:
            result.clear()
            result.append(arr[i])
            result.append(arr[i + 1])
            min_diff = arr[i + 1] - arr[i]
        elif arr[i + 1] - arr[i] == min_diff:
            result.append(arr[i])
            result.append(arr[i + 1])
    return result


print(closestNumbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]))  # [-20, 30]
