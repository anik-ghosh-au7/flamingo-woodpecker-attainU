# Solution 1

# from collections import Counter
#
#
# def missingNumbers(arr, brr):
#     count = Counter(brr) - Counter(arr)
#     return sorted(count)


# Solution 2

# def missingNumbers(arr, brr):
#     result_ = []
#     for i in set(brr):
#         if brr.count(i) - arr.count(i) > 0:
#             result_.append(i)
#     return sorted(result_)


# Solution 3

def missingNumbers(arr, brr):
    dict_ = {}
    result_ = []
    for i in brr:
        if i not in dict_:
            dict_[i] = 1
        else:
            dict_[i] += 1
    for j in arr:
        dict_[j] -= 1
    for k in dict_:
        if dict_[k] > 0:
            result_.append(k)
    return sorted(result_)




if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)
    print(result)
