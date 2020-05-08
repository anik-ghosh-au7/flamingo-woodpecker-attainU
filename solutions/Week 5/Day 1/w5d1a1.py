class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def quick_sort_rec(elms):
    return LinkedList.quick_sort(elms)


class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.end = self.head
            return
        else:
            self.end.next = Node(data)
            self.end = self.end.next
            return

    def display(self):
        curr_node = self.head
        while curr_node is not None:
            print('\033[46m', curr_node.data, '\033[41m', end=" --\033[0m-->")
            curr_node = curr_node.next
        else:
            print('\033[44m', "None", '\033[0m')
            print()

    def quick_sort(self):
        if self.head is self.end:
            return self.head

        curr_node = self.head
        pivot = self.end
        lower_elms = LinkedList()
        higher_elms = LinkedList()

        while curr_node is not self.end:
            if curr_node.data <= pivot.data:
                lower_elms.append(curr_node.data)
                curr_node = curr_node.next
            else:
                higher_elms.append(curr_node.data)
                curr_node = curr_node.next
        quick_sort_rec(lower_elms)
        quick_sort_rec(higher_elms)

        # concat operation
        if lower_elms.end:
            lower_elms.end.next = pivot
            self.head = lower_elms.head
        else:
            self.head = pivot
        if higher_elms.end:
            pivot.next = higher_elms.head
            self.end = higher_elms.end
        else:
            self.end = pivot
            pivot.next = None


lis = LinkedList()
list1 = "18 5 11 30 19 5 6 2 3"
for i in list1.split():
    lis.append(int(i))
print()
print("Input : ", end="")
lis.display()
lis.quick_sort()
print("Output : ", end="")
lis.display()
