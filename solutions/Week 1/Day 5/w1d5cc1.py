# Solution 1


# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 != 0:
#             return True
#         elif year % 400 == 0:
#             return True
#     return False


# Solution 2

def is_leap(year):
    return True if (year % 4 == 0 and ((year % 100 != 0) or (year % 400 == 0))) else False


# -------------------------------------------------------------------------------------------------------------------------

# # Function call with 2000 as argument and printing the return value :
print(is_leap(2000))

# Output :
# True


# # Function call with 2022 as argument and printing the return value :
print(is_leap(2022))

# Output :
# False
