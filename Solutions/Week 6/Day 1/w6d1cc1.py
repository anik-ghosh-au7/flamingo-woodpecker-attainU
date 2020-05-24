# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def append(self, data):    # O(1)
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = self.end.next

    def pop(self):    # O(1)
        if self.head is None:
            return self.head
        else:
            temp_node = self.head
            self.head = self.head.next
            return temp_node


# Queue Class
class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, data):    # O(1)
        self.queue.append(data)

    def deque(self):    # O(1)
        return self.queue.pop().data

    def front_element(self):
        return self.queue.head.data

    def rear_element(self):
        return self.queue.end.data

    def is_empty(self):
        if self.queue.head is None:
            return True
        else:
            return False

    def show_queue(self):
        current_node = self.queue.head
        print("deque <--", end="")
        while current_node:
            print('\033[46m', current_node.data, '\033[41m', end=" --\033[0m-->")
            current_node = current_node.next
        else:
            print('\033[44m', "None", '\033[0m', end="")
            print("<-- enqueue")
            print()


que = Queue()
list1 = "18 5 11 30 19 5 6 2 3"
for i in list1.split():
    que.enqueue(int(i))
print()
print("Input Queue : ", end="")
que.show_queue()
print("Front elem of the queue i.e the first elem of the input, is the first to come out : ", que.deque())
print()
print("Modified Queue : ", end="")
que.show_queue()
print("Front Element : ", que.front_element())
print()
print("Rear Element : ", que.rear_element())
print()
print("Queue is empty : ", que.is_empty())
