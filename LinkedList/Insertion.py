class Node:
    def __init__(self, data):
        self.data = data  # stores the value
        self.next = None # pointer to the next node


def insert_at_beginning(self, new_data):
    new_node = Node(new_data)  # Create a new node
    new_node.next = self.head  # New node points to the current head
    self.head = new_node  # The new node becomes the head

def insert_at_end(self, new_data):
    new_node = Node(new_data)
    if self.head is None:  # If the list is empty
        self.head = new_node
        return
    last = self.head
    while last.next:  # Traverse to the last node
        last = last.next
    last.next = new_node  # The last node points to the new node
