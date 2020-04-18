# Solution 1


# def print_formatted(number):
#     width = len("{:b}".format(number))
#     for num in range(1, number + 1):
#         print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(num, w=width))


# Solution 2


def print_formatted(number):
    width = len(bin(number)[2:])
    for num in range(1, number + 1):
        dec = str(num)
        # oct_ = str(oct(num))[2:]
        # oct_ = str(oct(num)).lstrip('0o')
        oct_ = str(oct(num)).replace('0o', '')
        hex_ = str(hex(num)).replace('0x', '').upper()
        bin_ = str(bin(num)).replace('0b', '')

        print(dec.rjust(width), oct_.rjust(width), hex_.rjust(width), bin_.rjust(width), sep=' ')


# -------------------------------------------------------------------------------------------------------------------------

# calling function and passing 5 as argument
print_formatted(5)

# Output :
#   1   1   1   1
#   2   2   2  10
#   3   3   3  11
#   4   4   4 100
#   5   5   5 101
