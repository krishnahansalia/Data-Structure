#Test git commit
from datetime import datetime

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return str(self.data)


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    #this will insert data at the end, so we will manipulate it with O(1) running complexity
    def insert(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            #data will be inserted at the end of the list
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def traverse_forward(self):
        actual_node = self.head

        while actual_node:
            print(actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):
        actual_node = self.tail

        while actual_node:
            print(actual_node.data)
            actual_node = actual_node.previous

    def remove(self,data):
        if self.head is None:
            return
        
        actual_node = self.head
        previous_node = None

        while actual_node and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next 
            
        if actual_node is None:
            return

        if previous_node is None:
            self.head = actual_node.next
        else:
            previous_node.next = actual_node.next
            

doubly_linkedlist = DoublyLinkedList()
doubly_linkedlist.insert(10)
doubly_linkedlist.insert(60)
doubly_linkedlist.insert(600)
doubly_linkedlist.insert(6000)
doubly_linkedlist.insert("Mike")
print("-------Traverse Forward----------")
doubly_linkedlist.traverse_forward()
print("-------Traverse Backward----------")
doubly_linkedlist.traverse_backward()
doubly_linkedlist.remove(10)
print("Removed 10")
print("-------Traverse Forward----------")
doubly_linkedlist.traverse_forward()
doubly_linkedlist.remove(60)
print("Removed 60")
print("-------Traverse Forward----------")
doubly_linkedlist.traverse_forward()
print("--------- Remove---------")
doubly_linkedlist.remove("Mike")
print("Removed Mike")
doubly_linkedlist.traverse_forward()