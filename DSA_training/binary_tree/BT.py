class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = TreeNode(value)
            else:
                self._insert(current.left, value)
        else:
            if current.right is None:
                current.right = TreeNode(value)
            else:
                self._insert(current.right, value)

    def in_order_traversal(self):
        def _in_order(node):
            if node is None:
                return []
            return _in_order(node.left) + [node.value] + _in_order(node.right)
        return _in_order(self.root)

# Example Usage
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
print("In-order Traversal:", bst.in_order_traversal())
