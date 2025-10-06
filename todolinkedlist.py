

from node import Node
class LinkedList():
    def __init__(self):
        self.head = None
    
    def __str__(self):
        if self.head is None:
            return "Empty list"
        return str(self.head)
    
    def add_to_front(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
    
    def iterative_find(self, target):
        current = self.head
        while current is not None:
            if current.data == target:
                return current
            current = current.next
        return 
    
    def add_to_back(self, data):
        new_node = Node(data)
        
        # If list is empty — new node becomes the head
        if self.head is None:
            self.head = new_node
            return
        # , walk to the end
        current = self.head
        while current.next is not None:
            current = current.next
        
        # Set the last node’s .next to our new node
        current.next = new_node
    
    def remove_at_index(self, index):
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next # next node becomes the head
            return
        current = self.head
        prev = None
        count = 0

        while current is not None and count < index:
            prev = current
            current = current.next
            count += 1

        if current is not None: 
            return
        
        prev.next = current.next
    
    def clear(self):
        self.head = None
    
    def change_priority(self, index):
     return self.head.change_priority(index)

    def conditional_str(self, predicate):
        return self.head.conditional_str(predicate)

    def filter(self, predicate):
        return self.head.filter(predicate)