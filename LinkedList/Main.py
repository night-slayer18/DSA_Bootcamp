# Node class to represent each node in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # stores the value
        self.next = None  # pointer to the next node

# LinkedList class to represent the entire linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list

    # Insertion at the beginning of the linked list
    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)  # Create a new node
        new_node.next = self.head  # New node points to the current head
        self.head = new_node  # The new node becomes the head

    # Insertion at the end of the linked list
    def insert_at_end(self, new_data):
        new_node = Node(new_data)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node  # New node becomes the head
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = new_node  # The last node points to the new node

    # Deletion of a node by value
    def delete_node(self, key):
        current = self.head

        # If the node to be deleted is the head
        if current and current.data == key:
            self.head = current.next  # Move head to the next node
            current = None  # Free the memory (optional in Python)
            return

        # Otherwise, search for the node to delete
        prev = None
        while current and current.data != key:
            prev = current  # Move to next node
            current = current.next

        # If key was not present in the list
        if current is None:
            print(f"Element {key} not found in the list.")
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None  # Free the memory (optional in Python)

    # Traversal of the linked list (to print the elements)
    def traverse(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of the list

    # Search for an element in the linked list
    def search(self, key):
        current = self.head  # Start at the head of the list
        position = 0  # To track the position of the node
        while current:
            if current.data == key:
                return f"Element {key} found at position {position}"
            current = current.next
            position += 1
        return f"Element {key} not found in the list"


# Example usage of LinkedList class
if __name__ == "__main__":
    ll = LinkedList()

    # Inserting elements
    ll.insert_at_beginning(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)

    # Traversing the linked list
    print("Linked list after insertion:")
    ll.traverse()

    # Searching for an element
    print("\nSearch Results:")
    print(ll.search(20))  # Output: Element 20 found at position 1
    print(ll.search(50))  # Output: Element 50 not found in the list

    # Deleting an element
    print("\nDeleting 30:")
    ll.delete_node(30)

    # Traversing the linked list after deletion
    print("Linked list after deletion:")
    ll.traverse()
