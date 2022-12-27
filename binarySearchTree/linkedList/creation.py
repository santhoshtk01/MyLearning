# Program to create Binary Search Tree.
"""
Properties:
- The left child should be less than or equal to the root node.
- The right child should be greater than or equal to the root node.
"""


class BSTNode:
    """Class to represent a binary search tree node."""
    def __init__(self, value: int):
        self.value = value
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree:
    """Class to represent binary search tree."""
    def __init__(self, value: int):
        self.root = BSTNode(value)


if __name__ == "__main__":
    bst = BinarySearchTree(100)

