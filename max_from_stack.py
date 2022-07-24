#LIFO - Last In First Out
#Stack is the Abstract Data Type that's going to define the behavior and we will use 1-D array as an underline data structure
#get max item with O(1) but this need O(N) memory, we will store data in new stack along with original stack

class Stack:
    def __init__(self):
        #stack will be one dimensional array
        self.stack = []
        self.max_stack = []

    def push(self,data):
        self.stack.append(data)

        if self.stack_size() == 1:
            self.max_stack.append(data)

        if data > self.max_stack[-1]:
            self.max_stack.append(data)

    def get_max_item(self):
        return self.max_stack[-1]

    #remove and return last item inserted (LIFO), O(1) runtime
    def pop(self):
        if self.stack_size()<1:
            return
        data = self.stack[-1]
        del self.stack[-1]
        return data

    #returns last item without removing it, O(1) runtime
    def peek(self):
        if self.stack_size()<1:
            return
        return self.stack[-1]

    #O(1) runtime
    def is_empty(self):
        return self.stack == []

    #
    def stack_size(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(40)
stack.push(4)
stack.push(100)
stack.push(200)
stack.push(30000)
stack.push(400)
stack.push(50)
print("Max from stack :",stack.get_max_item())