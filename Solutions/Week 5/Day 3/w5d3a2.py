# Node Class
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
            self.end.next = self.head

    def insert(self, data, position):
        new_node = Node(data)
        if position == 1:
            curr_node = self.head
            self.head = new_node
            new_node.next = curr_node
        else:
            curr_node = self.head
            count = 1
            while count < position - 1:
                count += 1
                curr_node = curr_node.next
                # print(count, ' ---> ', curr_node.data)
        temp_node = curr_node.next
        curr_node.next = new_node
        new_node.next = temp_node

    def delete_position(self, position):
        if self.head is None:
            return self.head
        if position == 1:
            temp_node = self.head
            self.head = self.head.next
            return temp_node
        else:
            count = 1
            curr_node = self.head
            while count <= position - 2:  # to go till node before position
                count += 1
                curr_node = curr_node.next
            temp_node = curr_node.next
            curr_node.next = curr_node.next.next
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


# position of the elements starts from one
cl = CircularLinkedList()
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in lis:
    cl.append(i)
cl.display()
print("deleted element : ",
      cl.delete_position(1).data)  # deleted element : 1
print()
cl.display()  # 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
print("deleted element : ", cl.delete_position(1).data)  # deleted element : 2
print()
cl.display()  # 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
print("deleted element : ", cl.delete_position(3).data)  # deleted element : 5
print()
cl.display()  # 3 -> 4 -> 6 -> 7 -> 8 -> 9
