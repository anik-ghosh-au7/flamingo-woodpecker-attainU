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

    def pop(self):
        if self.head is None:
            return self.head
        elif self.head == self.end:
            temp_node = self.head
            self.head = None
            self.end = None
            return temp_node
        else:
            curr_node = self.head
            while curr_node.next is not self.end:
                curr_node = curr_node.next
            temp_node = self.end
            self.end = self.end.prev
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


lis = DoublyLinkedList()
list1 = "98826749"
for i in list1:
    lis.append(int(i))
lis.display()
print("deleted element : ", lis.pop().data, '\n')
lis.display()
print("deleted element : ", lis.pop().data, '\n')
lis.display()
print("deleted element : ", lis.pop().data, '\n')
lis.display()
