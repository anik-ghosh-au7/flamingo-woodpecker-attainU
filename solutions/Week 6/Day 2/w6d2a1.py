# Stack Class
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.insert(0, data)

    def pop(self):
        return self.stack.pop()

    def length(self):
        return len(self.stack)


# Queue Class
class Queue:
    def __init__(self):
        self.enqueue_stack = Stack()
        self.deque_stack = Stack()

    def enqueue(self, data):
        print('enqueueing %d into the queue' % data)
        self.enqueue_stack.push(data)

    def deque(self):
        if self.deque_stack.length() == 0:
            if self.enqueue_stack.length() == 0:
                return 'Queue is empty!!!'
            else:
                while self.enqueue_stack.length() >= 1:
                    self.deque_stack.push(self.enqueue_stack.pop())
                return self.deque_stack.pop()
        else:
            return self.deque_stack.pop()


que = Queue()
list1 = "5 6 2 3"
for i in list1.split():
    que.enqueue(int(i))
print(que.deque())  # 5
print(que.deque())  # 6
print(que.deque())  # 2
que.enqueue(7)
que.enqueue(9)
print(que.deque())  # 3
print(que.deque())  # 7
print(que.deque())  # 9
print(que.deque())  # Queue is empty!!!

