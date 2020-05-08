# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Circular Linked List Class
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.end = new_node
            self.end.next = self.head
        else:
            self.end.next = new_node
            self.end = self.end.next
            new_node.next = self.head

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
            self.end = curr_node
            self.end.next = self.head
            return temp_node

    def display(self):
        curr_node = self.head
        if self.head:
            while curr_node is not self.end:
                print('\033[46m', curr_node.data, '\033[41m', end=" --\033[0m-->")
                curr_node = curr_node.next
            else:
                print('\033[46m', self.end.data, '\033[41m', end=" --\033[0m-->")
                print('\033[44m', "Head", '\033[0m')
                print()
        else:
            print('\033[44m', "None", '\033[0m')


cl = CircularLinkedList()
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lis = [1]
for i in lis:
    cl.append(i)
cl.display()
print("deleted element : ", cl.pop().data)
print()
cl.display()
print("deleted element : ", cl.pop().data)
print()
cl.display()
print("deleted element : ", cl.pop().data)
print()
cl.display()
