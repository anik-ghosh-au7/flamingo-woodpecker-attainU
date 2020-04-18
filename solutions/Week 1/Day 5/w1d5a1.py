# Solution 1


# def largest_plaindrome(n):
#     num1, num2 = 0, 0
#     for _ in range(n):
#         num1 = (num1 * 10) + 9
#         num2 = (num2 * 10) + 9
#     while num1 > 0:
#         while num2 > 0:
#             result = num1 * num2
#             temp = result
#             rev = 0
#             while result > 0:
#                 dig = result % 10
#                 rev = rev * 10 + dig
#                 result = result // 10
#             if temp == rev:
#                 return temp
#             num2 -= 1
#         num1 -= 1
#
#
# num = int(input("Enter the number of digits : "))
# print(largest_plaindrome(num))


# Solution 2 (Using string inbuilt method)


def largest_plaindrome(n):
    num1 = int('9' * n)
    num2 = int('9' * n)
    while num1 > 0:
        while num2 > 0:
            if str(num1 * num2) == str(num1 * num2)[::-1]:
                return num1 * num2
            num2 -= 1
        num1 -= 1


num = int(input("Enter the number of digits : "))
print(largest_plaindrome(num))


# -------------------------------------------------------------------------------------------------------------------------

# Input :
# Enter the number of digits : 2

# Output :
# 9009


# Input :
# Enter the number of digits : 3

# Output :
# 90909
