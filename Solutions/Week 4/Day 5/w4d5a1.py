def counting_sort(arr):
    pass


counting_sort([1, 2, 7, 5, 4, 8, 9, 5, 4, 4])
# here we will apply counting sort algorithm because the value of each element falls within the range of len(arr)
# time complexity of O(n+k) where n is the number of elements in input array and k is the range of input.


def merge_sort(arr):
    pass


merge_sort([22, 333, 5746, 83, 79, 53, 75, 5746, 22])
# here we will apply merge sort algorithm list contains duplicate elements so we need it to be stable
# time complexity of O(nlog n)


def quick_sort(arr):
    pass


quick_sort([22, 333, 5746, 83, 79, 53, 75, 7564, 4674, 97, 542, 953])
# here we will apply quick sort algorithm list does not contains duplicate elements so there is no need for it to be stable
# and quick sort is easier to implement
# time complexity of O(nlog n)


def bubble_sort(arr):
    pass


bubble_sort([22, 11, 333, 444, 5555, 6672, 7894])
# here we will apply bubble sort algorithm only the first two elements of the list is not sorted so after one step there
# will be no swapping and we can stop the program execution
# time complexity of O(n^2) for normal case but for this one O(c)


def selection_sort(arr):
    pass


selection_sort([6083, 333, 444, 5555, 11, 6672, 7894])
# here we will apply selection sort algorithm only the one element i.e the min one 11 is not in correct position
# and it is in the position where the 6083 should be so after one swapping there is no need to continue the execution
# time complexity of O(n^2) for normal case but for this one O(c)
