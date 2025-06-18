'''
This would help to create linked list as and when needed in other programs

Linked Lists has 2 parts
1. Data
2. Reference to the next node

it's something like
|1|address|-->|2|address|-->|3|address|
'''

# We need to create a node that would store the data and would point to the next node

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None # currently it is pointing to nothing

# Let's try to create a structure for our linked list

class LinkedList:
    def __init__(self):
        self.head = None #there is no head currently

    # creating append to add data to our linked list
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def show(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print("None")