# Search for a key in a binary search tree (BST) using recursion

def search(self, key):
    return self._search_recursively(self.root, key)

def _search_recursively(self, node, key):
    if node is None or node.val == key:  # Key found or reached end
        return node
    if key < node.val:  # Key is smaller, search left
        return self._search_recursively(node.left, key)
    return self._search_recursively(node.right, key)  # Search right
