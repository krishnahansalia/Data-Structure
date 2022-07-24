from os import link


class Node:

    def __init__(self,data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)

    
class LinkedList:

    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    #O(1) Constant running time
    def insert_start(self,data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is not None:
            #New node will point to previous First node
            new_node.next_node = self.head

        #LinkedList will make new Node as the Head Node. So, update the reference
        self.head = new_node

    #O(N) to insert data at the end of LinkedList
    def insert_end(self,data):
        self.num_of_nodes += 1
        new_node = Node(data)

        #Check if LinkedList is empty
        if self.head is None:
            self.head = new_node
        else:
            actual_node = self.head

            #O(N) linear running time complexity
            while actual_node.next_node:
                actual_node = actual_node.next_node

            actual_node.next_node = new_node
    
    #O(1) constant running time
    def size_of_list(self):
        return self.num_of_nodes

    #O(N) linear Runtime to traverse through the LinkedList
    def traverse(self):
        actual_node = self.head

        while actual_node:
            print(actual_node)
            actual_node = actual_node.next_node

    #O(N) linear running time comlexity
    def remove(self,data):
        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node
            
        if actual_node is None:
            return

        #Update the references
        if previous_node is None:
            #remove head node
            self.head = actual_node.next_node
        else:
            #remove internal node
            previous_node.next_node = actual_node.next_node

    def get_middle_node(self):
        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            slow_pointer = slow_pointer.next_node
            fast_pointer = fast_pointer.next_node.next_node

        return slow_pointer

    def reverse(self):
        if self.head is None:
            return
        
        current_node = self.head
        previous_node = None
        next_node = None

        while current_node:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_start(10)
    linked_list.insert_start(50)
    linked_list.insert_start("Adam")
    linked_list.insert_end("Mike")
    linked_list.insert_start(1.2)
    linked_list.insert_end(1000)
    linked_list.traverse()
    print("Middle Node :",linked_list.get_middle_node())
    print("----------Reverse the list----------")
    linked_list.reverse()
    linked_list.traverse()
    print("------------")
    linked_list.remove(1000)
    linked_list.traverse()
    print("------------")
    linked_list.remove(1.2)
    linked_list.traverse()
    print("------------")
    linked_list.remove(50)
    linked_list.traverse()
    print("------------")
    linked_list.remove("Steve")
    linked_list.traverse()