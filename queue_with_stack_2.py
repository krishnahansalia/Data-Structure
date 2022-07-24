#Queue - FIFO : First In First Out 
class Queue:

    def __init__(self):
        self.stack = []

    def enqueue(self,data):
        self.stack.append(data)

    def dequeue(self):
        if len(self.stack)==1:
            return self.stack.pop()

        if len(self.stack) == 0:
            return "Stack is empty"
        else:
            item = self.stack.pop()
            data = self.dequeue()

        return data

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())