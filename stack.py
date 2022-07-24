#LIFO - Last In First Out
#Stack is the Abstract Data Type that's going to define the behavior and we will use 1-D array as an underline data structure

class Stack:
    def __init__(self):
        #stack will be one dimensional array
        self.stack = []

    def push(self,data):
        self.stack.append(data)

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
print("Stack Size :",stack.stack_size())
print("Peeked Item :",stack.peek())
print("Stack Size :",stack.stack_size())
print("Popped data :",stack.pop())
print("Stack Size after popping data:",stack.stack_size())
print("Is Stack empty :",stack.is_empty())
