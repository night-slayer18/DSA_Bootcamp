def delete_node(self, key):
    current = self.head
    if current and current.data == key:  # If the node to be deleted is the head
        self.head = current.next
        current = None
        return
    
    prev = None
    while current and current.data != key:  # Traverse to find the node
        prev = current
        current = current.next

    if current is None:  # If the key is not present
        return

    prev.next = current.next  # Unlink the node from the linked list
    current = None
