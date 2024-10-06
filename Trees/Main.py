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

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)  # Print right subtree
            print(' ' * 4 * level + '-> ' + str(node.val))  # Print current node
            self.print_tree(node.left, level + 1)  # Print left subtree

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)  # Traverse left subtree
            print(node.val, end=" ")  # Visit the node
            self.inorder_traversal(node.right)  # Traverse right subtree

    def preorder_traversal(self, node):
        if node:
            print(node.val, end=" ")  # Visit the node
            self.preorder_traversal(node.left)  # Traverse left subtree
            self.preorder_traversal(node.right)  # Traverse right subtree

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)  # Traverse left subtree
            self.postorder_traversal(node.right)  # Traverse right subtree
            print(node.val, end=" ")  # Visit the node

    def search(self, key):
        return self._search_recursively(self.root, key)

    def _search_recursively(self, node, key):
        if node is None or node.val == key:  # Key found or reached end
            return node
        if key < node.val:  # Key is smaller, search left
            return self._search_recursively(node.left, key)
        return self._search_recursively(node.right, key)  # Search right

    def delete_node(self, key):
        self.root = self._delete_recursively(self.root, key)

    def _delete_recursively(self, node, key):
        if node is None:  # Base case
            return node
        if key < node.val:  # Key is smaller, go left
            node.left = self._delete_recursively(node.left, key)
        elif key > node.val:  # Key is greater, go right
            node.right = self._delete_recursively(node.right, key)
        else:  # Node with the key found
            if node.left is None:  # Node with only right child
                return node.right
            elif node.right is None:  # Node with only left child
                return node.left

            # Node with two children: Get the inorder successor
            min_node = self._find_min(node.right)
            node.val = min_node.val  # Copy the inorder successor's value to this node
            node.right = self._delete_recursively(node.right, min_node.val)  # Delete the inorder successor

        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:  # Loop to find the leftmost leaf
            current = current.left
        return current


# Example usage of BinarySearchTree class
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Inserting elements into the binary search tree
    elements = [50, 30, 20, 40, 70, 60, 80]
    for elem in elements:
        bst.insert(elem)

    # Print the tree structure after insertions
    print("Tree Structure After Insertions:")
    bst.print_tree(bst.root)

    # Traversing the binary search tree
    print("\nInorder Traversal:")
    bst.inorder_traversal(bst.root)
    print("\nPreorder Traversal:")
    bst.preorder_traversal(bst.root)
    print("\nPostorder Traversal:")
    bst.postorder_traversal(bst.root)

    # Searching for an element
    print("\n\nSearch Results:")
    if bst.search(40):
        print("Element 40 found in the tree.")
    else:
        print("Element 40 not found in the tree.")

    # Deleting an element
    print("\nDeleting 20:")
    bst.delete_node(20)
    print("Inorder Traversal after deletion:")
    bst.inorder_traversal(bst.root)

    # Print the tree structure after deletion
    print("\nTree Structure After Deletion:")
    bst.print_tree(bst.root)
