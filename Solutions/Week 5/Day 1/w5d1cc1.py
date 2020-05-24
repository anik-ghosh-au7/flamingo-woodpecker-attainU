# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            # to do append operation in O(1)
            self.end = self.head
            return
        else:
            self.end.next = Node(data)
            self.end = self.end.next

        # this will perform the append operation in O(n)
        # else:
        #     curr_node = self.head
        #     while curr_node.next is not None:
        #         curr_node = curr_node.next
        #     curr_node.next = Node(data)

    # def print_head_end(self):
    #     print(self.head.data)
    #     print(self.end.data)

    def pair_swap(self):
        curr_node = self.head
        if curr_node is self.end:
            return self.head
        while curr_node is not None and curr_node.next is not None:
            curr_node.data, curr_node.next.data = curr_node.next.data, curr_node.data
            curr_node = curr_node.next.next

    def display(self):
        curr_node = self.head
        while curr_node is not None:
            print('\033[46m', curr_node.data, '\033[41m', end=" --\033[0m-->")
            curr_node = curr_node.next
        else:
            print('\033[44m', "None", '\033[0m')
            print()


lis = LinkedList()
list1 = "18 5 11 30 19 5 6 2 3"
for i in list1.split():
    lis.append(int(i))
# lis.print_head_end()
print()
print("Input : ", end="")
lis.display()
lis.pair_swap()
print("Output : ", end="")
lis.display()

# -------------------------------- explanation -------------------------------------------

#   Explanation for pair_swap()

#   Inside pair_swap()
#   Input
#   curr/head                                           end
#   18 --> 5 --> 11 --> 30 --> 19 --> 5 --> 6 --> 2 --> 3 --> None

#   Loop - PASS - 1
#   curr/head                                           end
#   5 --> 18 --> 11 --> 30 --> 19 --> 5 --> 6 --> 2 --> 3 --> None

#   Loop - PASS - 2
#   head         curr                                   end
#   5 --> 18 --> 30 --> 11 --> 19 --> 5 --> 6 --> 2 --> 3 --> None

#   Loop - PASS - 3
#   head                       curr                     end
#   5 --> 18 --> 30 --> 11 --> 5 --> 19 --> 6 --> 2 --> 3 --> None

#   Loop - PASS - 4
#   head                                    curr        end
#   5 --> 18 --> 30 --> 11 --> 5 --> 19 --> 2 --> 6 --> 3 --> None

#   Loop - PASS - 5
#   head                                                curr/end
#   5 --> 18 --> 30 --> 11 --> 5 --> 19 --> 2 --> 6 --> 3 --> None

#   Loop breaks
#   As curr.next is None
