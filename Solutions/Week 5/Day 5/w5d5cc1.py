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

    def reverse(self):  # Time complexity O(n)

        prev_node = None
        curr_node = self.head
        if curr_node is None:
            return curr_node
        while curr_node is not None:
            next_node, curr_node.next = curr_node.next, prev_node
            prev_node, curr_node = curr_node, next_node
        self.end = self.head
        self.head = prev_node

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
ll.reverse()
ll.display()

# ------------------------------- explanation [reverse()] -----------------------------------------

#   Input
#   Head
#   18 --> 5 --> 11 --> 30 --> 5 --> None

#   Inside reverse()
#   Prev     Curr/Head
#   None     18 --> 5 --> 11 --> 30 --> 5 --> None

#   Loop - PASS - 1
#   P        C/H    Next
#   None <-- 18     5 --> 11 --> 30 --> 5 --> None
#            P/H    C/Next
#   None <-- 18     5 --> 11 --> 30 --> 5 --> None

#   Loop - PASS - 2
#            P/H    C     N
#   None <-- 18 <-- 5     11 --> 30 --> 5 --> None
#            H      P     C/N
#   None <-- 18 <-- 5     11 --> 30 --> 5 --> None

#   Loop - PASS - 3
#            H      P     C      N
#   None <-- 18 <-- 5 <-- 11     30 --> 5 --> None
#            H            P      C/N
#   None <-- 18 <-- 5 <-- 11     30 --> 5 --> None

#   Loop - PASS - 4
#            H            P      C      N
#   None <-- 18 <-- 5 <-- 11 <-- 30     5 --> None
#            H                   P      C/N
#   None <-- 18 <-- 5 <-- 11 <-- 30     5 --> None

#   Loop - PASS - 5
#            H                   P      C     N
#   None <-- 18 <-- 5 <-- 11 <-- 30 <-- 5     None
#            H                          P     C/N
#   None <-- 18 <-- 5 <-- 11 <-- 30 <-- 5     None

#   Loop breaks
#            E                        H/P
#   None <-- 18 <-- 5 <-- 11 <-- 30 <-- 5

#   Output
#   Head
#   5 --> 30 --> 11 --> 5 --> 18 --> None
