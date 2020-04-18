# # Solution 1


# def print_rangoli(size):
#     value_a = ord('a')
#
#     for i in range(0, size):
#
#         print("-" * ((2 * (size - i)) - 2), end="")
#         for j in range(0, i + 1):
#             if j > 0:
#                 print("-", end="")
#             print(chr(value_a + (size - j - 1)), end="")
#
#         for k in range(i, 0, -1):
#             print("-", end="")
#             print(chr(value_a + (size - k)), end="")
#
#         print("-" * ((2 * (size - i)) - 2))
#
#     for i in range(size - 2, -1, -1):
#
#         print("-" * ((2 * (size - i)) - 2), end="")
#         for j in range(0, i + 1):
#             if j > 0:
#                 print("-", end="")
#             print(chr(value_a + (size - j - 1)), end="")
#
#         for k in range(i, 0, -1):
#             print("-", end="")
#             print(chr(value_a + (size - k)), end="")
#
#         print("-" * ((2 * (size - i)) - 2))


# Solution 2


def print_rangoli(size):
    str_list = 'abcdefghijklmnopqrstuvwxyz'[0:size]

    for i in range(size - 1, -size, -1):
        x = abs(i)
        line = str_list[size:x:-1] + str_list[x:size]
        print("--" * x + '-'.join(line) + "--" * x)


# -------------------------------------------------------------------------------------------------------------------------

# Function call with 5 as argument :
print_rangoli(5)

# Output :
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
