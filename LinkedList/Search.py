def search(self, key):
        current = self.head  # Start at the head of the list
        position = 0  # To track the position of the node
        while current:
            if current.data == key:
                return f"Element {key} found at position {position}"
            current = current.next
            position += 1
        return f"Element {key} not found in the list"