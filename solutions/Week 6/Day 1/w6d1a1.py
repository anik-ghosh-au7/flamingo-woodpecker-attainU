# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        # self.end = None

    def push(self, data):    # O(1)
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            # self.end = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):    # O(1)
        if self.head is None:
            return self.head
        else:
            temp_node = self.head
            self.head = self.head.next
            return temp_node


# Queue Class
class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, data):    # O(1)
        self.stack.push(data)

    def pop(self):    # O(1)
        return self.stack.pop().data

    def peek(self):
        return self.stack.head.data

    def is_empty(self):
        if self.stack.head is None:
            return True
        else:
            return False

    def show_stack(self):
        current_node = self.stack.head
        print("<==>", end="")
        while current_node:
            print('\033[46m', current_node.data, '\033[41m', end=" --\033[0m-->")
            current_node = current_node.next
        else:
            print('\033[44m', "None", '\033[0m', end="")
            print('\n\n')


stk = Stack()
list1 = "18 5 11 30 19 5 6 2 3"
for i in list1.split():
    stk.push(int(i))
print()
print("Input Stack : ", end="")
stk.show_stack()
print("First elem to come out of the stack, is the last elem of the input : ", stk.pop())
print()
print("Modified Stack : ", end="")
stk.show_stack()
print("Peek Element : ", stk.peek())
print()
print("Stack is empty : ", stk.is_empty())
