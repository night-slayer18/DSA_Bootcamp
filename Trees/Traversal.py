# Inorder Traversal (Left, Root, Right)
# Prints the nodes in ascending order.

def inorder_traversal(self, node):
    if node:
        self.inorder_traversal(node.left)  # Traverse left subtree
        print(node.val, end=" ")  # Visit the node
        self.inorder_traversal(node.right)  # Traverse right subtree


# Preorder Traversal (Root, Left, Right)
# Visits the node before its children.

def preorder_traversal(self, node):
    if node:
        print(node.val, end=" ")  # Visit the node
        self.preorder_traversal(node.left)  # Traverse left subtree
        self.preorder_traversal(node.right)  # Traverse right subtree


# Postorder Traversal (Left, Right, Root)
# Visits the node after its children.

def postorder_traversal(self, node):
    if node:
        self.postorder_traversal(node.left)  # Traverse left subtree
        self.postorder_traversal(node.right)  # Traverse right subtree
        print(node.val, end=" ")  # Visit the node


