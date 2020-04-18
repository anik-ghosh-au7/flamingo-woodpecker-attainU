# # Solution 1
#
#
# def grade_students(lis):
#     sum_marks = 0
#
#     for i in lis:
#         sum_marks += i
#
#     average = sum_marks / len(lis)
#
#     if average > 90:
#         grade = 'A'
#     elif average > 80:
#         grade = 'B'
#     elif average > 60:
#         grade = 'C'
#     elif average > 40:
#         grade = 'D'
#     else:
#         grade = 'E'
#
#     return grade
#
#
# input_list = [int(i) for i in input('Enter the 5 numbers separated by space : ').split(' ')]
# print('The student\'s grade is :', grade_students(input_list))

# -------------------------------------------------------------------------------------------------------------------------

# Solution 2


from functools import reduce


def grade_students(lis):
    average = reduce(lambda a, b: a + b, lis) / len(lis)
    grade = 'A' if average > 90 else 'B' if average > 80 else 'C' if average > 60 else 'D' if average > 40 else 'E'
    return grade


input_list = [int(i) for i in input('Enter the 5 numbers separated by space : ').split(' ')]
print('The student\'s grade is :', grade_students(input_list))

# -------------------------------------------------------------------------------------------------------------------------

# Input :
# Enter the 5 numbers separated by space : 90 80 80 100 100

# Output :
# The student's grade is : B
