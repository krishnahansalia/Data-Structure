#FIFO - First In First Out
class Queue:

    def __init__(self):
        self.queue = []

    #O(1) runtime
    def is_empty(self):
        return self.queue == []

    #O(1) runtime complexity, append data at the end of list
    def enqueue(self,data):
        self.queue.append(data)

    #O(N) runtime complexity, 
    def dequeue(self):
        if self.size_queue() != 0:
            data = self.queue[0]
            del self.queue[0]
            return data

    #O(1) runtime complexity
    def peek(self):
        if self.size_queue() != 0:
            return self.queue[0]

    #O(1) runtime complexity
    def size_queue(self):
        return len(self.queue)

    def show_queue(self):
        print(self.queue)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue("Mike")
queue.enqueue("Steve")
print("--------------")
queue.show_queue()
print("--------------")
print("Queue Size :",queue.size_queue())
print("Now Deque")
queue.dequeue()
print("--------------")
queue.show_queue()
print("--------------")
print("Queue Size after dequeue:",queue.size_queue())
print("Peek from queue :",queue.peek())
print("Queue Size after peek:",queue.size_queue())
print("--------------")
queue.show_queue()
print("--------------")
print("Now Deque")
queue.dequeue()
print("Now Deque")
print("Queue Size after dequeue:",queue.size_queue())
queue.dequeue()
print("Now Deque")
print("Queue Size after dequeue:",queue.size_queue())
queue.dequeue()
print("Queue Size after dequeue:",queue.size_queue())
queue.dequeue()
print("Queue Size after dequeue:",queue.size_queue())