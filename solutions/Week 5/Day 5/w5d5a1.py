# # Node class
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# # Linked List class
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.end = None
#
#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             self.end = new_node
#         else:
#             self.end.next = new_node
#             self.end = self.end.next
#
#     def reverse(self, k, c=0):  # Time complexity O(n)
#
#         prev_node = None
#         curr_node = self.head
#         count = 0
#         if curr_node is None:
#             return curr_node
#         print('count', c)
#         for _ in range(c):
#             if curr_node.next is not None:
#                 curr_node = curr_node.next
#
#         while curr_node is not None and count < k:
#             next_node, curr_node.next = curr_node.next, prev_node
#             prev_node, curr_node = curr_node, next_node
#             count += 1
#         c += k
#         if next_node is not None:
#             self.reverse(k, c)
#         # self.end = self.head
#         # self.head = prev_node
#
#     def display(self):
#         curr_node = self.head
#         while curr_node is not None:
#             print('\033[46m', curr_node.data, '\033[41m', end=" --\033[0m-->")
#             curr_node = curr_node.next
#         else:
#             print('\033[44m', "None", '\033[0m')
#             print()
#
#
# ll = LinkedList()
# lis = [18, 5, 11, 30, 5]
# for i in lis:
#     ll.append(i)
# ll.display()
# ll.reverse(2)
# ll.display()


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = self.end.next


    def display(self):
        curr_node = self.head
        while curr_node is not None:
            print('\033[46m', curr_node.data, '\033[41m', end=" --\033[0m-->")
            curr_node = curr_node.next
        else:
            print('\033[44m', "None", '\033[0m')
            print()


ll = LinkedList()
lis = [18, 5, 11, 30, 5]
for i in lis:
    ll.append(i)
ll.display()


def reverse(head, k):

    curr_node = head
    prev_node = None

    count = 0
    while count < k and curr_node is not None:
        next_node, curr_node.next = curr_node.next, prev_node
        prev_node, curr_node = curr_node, next_node
        count += 1

    if head is not None:
        head.next = reverse(curr_node, k)

    return prev_node


ll.head = reverse(ll.head, 2)
ll.display()
