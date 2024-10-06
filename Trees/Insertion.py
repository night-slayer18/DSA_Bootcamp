class Node:
    def __init__(self, key):
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child
        self.val = key  # Node value


class BinarySearchTree:
    def __init__(self):
        self.root = None  # Initialize the root of the tree

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)  # Create root node
        else:
            self._insert_recursively(self.root, key)  # Insert recursively

    def _insert_recursively(self, node, key):
        if key < node.val:  # If key is smaller, go left
            if node.left is None:
                node.left = Node(key)  # Create new node
            else:
                self._insert_recursively(node.left, key)  # Recur on left child
        else:  # If key is greater or equal, go right
            if node.right is None:
                node.right = Node(key)  # Create new node
            else:
                self._insert_recursively(node.right, key)  # Recur on right child
