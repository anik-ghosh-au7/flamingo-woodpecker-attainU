# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.end = self.head
            return
        self.end.next = Node(data)
        self.end.next.prev = self.end
        self.end = self.end.next

    def delete_position(self, position):
        if self.head is None:
            return self.head
        if position == 1:
            temp_node = self.head
            self.head = self.head.next
            self.head.next.prev = self.head
            return temp_node
        else:
            count = 1
            curr_node = self.head
            while count <= position - 2:  # to go till node before position
                count += 1
                curr_node = curr_node.next
            temp_node = curr_node.next
            curr_node.next = curr_node.next.next
            curr_node.next.prev = curr_node
            return temp_node

    def display(self):
        curr_node = self.head
        if self.head:
            while curr_node is not self.end:
                print('\033[46m', curr_node.data, '\033[41m', end=" <==\033[0m==\033[47m==> ")
                curr_node = curr_node.next
            else:
                print('\033[46m', self.end.data, '\033[41m', end=" <==\033[0m==\033[47m==> ")
                print('\033[44m', "None", '\033[0m')
                print()
        else:
            print('\033[44m', "None", '\033[0m')


# position of the elements starts from one
dl = DoublyLinkedList()
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in lis:
    dl.append(i)
dl.display()
print("deleted element : ",
      dl.delete_position(1).data)  # deleted element : 1
print()
dl.display()  # 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
print("deleted element : ", dl.delete_position(1).data)  # deleted element : 2
print()
dl.display()  # 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
print("deleted element : ", dl.delete_position(3).data)  # deleted element : 5
print()
dl.display()  # 3 -> 4 -> 6 -> 7 -> 8 -> 9
