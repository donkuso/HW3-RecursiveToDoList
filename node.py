from task import Task 
import copy

class Node:
    def __init__(self, data: Task, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        if self.next is None:
            return str(self.data)
        return f"{self.data} --> {self.next}"
    
    def change_priority(self, index):
        if index == 0:
            self.data.update_priority()
            return
        if self.next is not None:
            self.next.change_priority(index-1)
        else:
            print("Index out of range")
    
    def conditional_str(self, condition):
        """
        condition: 
        returns: 
        """
        #base case (if this is the last node)
        if self.next is None:
            if condition(self):
                return str(self.data) + " --> None"     
            else:
                return "None"
        #Recursive case: there is a next node
        if condition(self):
            return str(self.data) + " --> " + self.next.conditional_str(condition)
        else:
            return self.next.conditional_str(condition)

    def filter(self, condition):
        """
        Takes in a condition that returns true/false that is used to filter self
        Creates a new linked list containing copies of Node objects
        Returns the head of the node that links the list
        """
        # Base case
        if self is None:
            return None
        
        # Recursive case
        if condition(self):
            if self.next is not None:
                return Node(self.data, self.next.filter(condition))
            else:
                return Node(self.data) # last node
        else:
            if self.next is not None:
                return self.next.filter(condition)
            else:
                return None