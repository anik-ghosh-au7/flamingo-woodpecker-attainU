# Queue Class
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def deque(self):
        return self.queue.pop(0)

    def length(self):
        return len(self.queue)


# Stack Class
class Stack:
    def __init__(self):
        self.queue_1 = Queue()
        self.queue_2 = Queue()

    def push(self, data):
        print('pushing %d to stack' % data)
        self.queue_1.enqueue(data)

    def pop(self):
        if self.queue_1.length() == 0:
            return None
        while self.queue_1.length() > 1:
            self.queue_2.enqueue(self.queue_1.deque())
        self.queue_1, self.queue_2 = self.queue_2, self.queue_1
        return self.queue_2.deque()


stk = Stack()
list1 = "5 6 2 3"
for i in list1.split():
    stk.push(int(i))
print(stk.pop())  # 3
print(stk.pop())  # 2
stk.push(9)
stk.push(73)
print(stk.pop())  # 73
print(stk.pop())  # 9
print(stk.pop())  # 6
print(stk.pop())  # 5
print(stk.pop())  # None
