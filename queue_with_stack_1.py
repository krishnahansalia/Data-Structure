#FIFO : First In First Out
class Queue:

    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    #O(1) runtime complexity
    def enqueue(self,data):
        self.enqueue_stack.append(data)

    def dequeue(self):
        if len(self.enqueue_stack)==0 and len(self.dequeue_stack)==0:
            return "Stacks are Empty"

        if len(self.dequeue_stack)==0:
            while len(self.enqueue_stack):
                self.dequeue_stack.append(self.enqueue_stack.pop())

        return self.dequeue_stack.pop()

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.dequeue())
queue.enqueue(5)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())