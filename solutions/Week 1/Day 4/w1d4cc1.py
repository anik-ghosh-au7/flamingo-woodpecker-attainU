# Solution 1


# def print_rangoli(size):
#     print('a' * size)
#     for i in range(1, size, 2):
#         print('a' * ((size - i)//2) + ' ' * i + 'a' * ((size - i)//2))
#         # print((' ' * i).center(size, 'a'))
#     for i in range(size-4, -1, -2):
#         print('a' * ((size - i)//2) + ' ' * i + 'a' * ((size - i)//2))
#         # print((' ' * i).center(size, 'a'))
#     print('a' * size)


# Solution 2


def print_rangoli(size):
    for i in range(size):
        if not i/2 == i//2 or i == 0:
            print((' ' * i).center(size, 'a'))
    for i in range(size-3, -1, -1):
        if not i/2 == i//2 or i == 0:
            print((' ' * i).center(size, 'a'))


# -------------------------------------------------------------------------------------------------------------------------

# Function call with 7 as argument :
print_rangoli(7)

# Output :
# aaaaaaa
# aaa aaa
# aa   aa
# a     a
# aa   aa
# aaa aaa
# aaaaaaa
