class LinkedList:
    def __init__(self):
        self.head = None  # The list starts empty

    # Traversal method
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of list
