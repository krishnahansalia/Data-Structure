#Test git commit
from multiprocessing import parent_process

class Node:

    def __init__(self,data,parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        #Going to be cruicial When implementing the remove function
        self.parent = parent

class BinarySearchTree:

    def __init__(self):
        #We can access root node exclusively
        self.root = None
        
    def insert(self,data):
        #First Node in the Binary Search Tree
        if self.root is None:
            self.root = Node(data)
        #Binary Search Tree is not Empty
        else:
            self.insert_node(data,self.root)

    def insert_node(self,data,node):
        #Go to left Sub tree
        if data < self.root:
            if node.left_node:
                #if left node exists, then we keep going
                self.insert_node(data,node.left_node)
            else:
                #there is no/no further left child and we will create one
                self.left_node = Node(data,node)
        #We have to go to right tree
        else:
            if node.right_node:
                self.insert_node(data,node.right_node)
            else:
                self.right_node = Node(data,node)

    def get_min(self):

        if self.node is None:
            return None

        else:
            while self.node:
                