# Solution 1 (using for loop)
#
#
# def fibonacci(n):
#     if n <= 1:
#         return [1]
#     arr = [1, 1]
#     for i in range(2, n):
#         if arr[i-1] + arr[i-2] > n:
#             break
#         arr.append(arr[i-1] + arr[i-2])
#     return arr
#
#
# print(*fibonacci(50))

# -------------------------------------------------------------------------------------------------------------------------

# Solution 2 (using recursion & without using any loops)


def rec_fibonacci(n, n2=1, n1=1):
    if n == 0:
        return
    else:
        a = n1 + n2
        if a > n + 2:
            return
        print(a, end=" ")
        return rec_fibonacci(n-1, a, n2)


def fib(n):
    if n <= 1:
        print(1, end=' ')
    else:
        print(1, 1, end=' ')
        rec_fibonacci(n-2)


fib(50)

# -------------------------------------------------------------------------------------------------------------------------

# Output : 1 1 2 3 5 8 13 21 34 
