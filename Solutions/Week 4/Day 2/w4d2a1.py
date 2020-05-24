# Both Solutions will give the correct result


# Solution 1 will give timeout for some test cases

# def superDigit(n, k):
#     start_num = sum(int(i) for i in (n*k))
#     return calculate(str(start_num))
#
#
# def calculate(num_str):
#     if len(num_str) == 1:
#         return int(num_str)
#     result = sum(int(i) for i in num_str)
#     return calculate(str(result))
#
#
# print(superDigit('148', 3))


# Solution 2 will work for all test cases

def superDigit(n, k):
    start_num = sum(int(i) for i in n) * k
    return calculate(str(start_num))


def calculate(num_str):
    if len(num_str) == 1:
        return int(num_str)
    result = sum(int(i) for i in num_str)
    return calculate(str(result))


print(superDigit('148', 3))


# ------------------------ explanation -----------------------

# so as per the first sample input, the value of n = 148 and value of k = 3

# so according to the first solution superDigit() is first multiplying the string i.e 148, k times ie 3
# and then calculating the sum of 1 4 8 1 4 8 1 4 8 to pass to calculate(), i.e calculate(36)

# but for the in the second solution it is first calculating the sum of 1 4 8 and then multiplying the result with 3
# to pass to calculate(), i.e calculate(36)
