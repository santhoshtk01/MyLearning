# Program to create a binary tree using python linked list.


class BinaryTreeNode:
    """
    Class for binary tree node.
    Attributes:
        - data (int) : The value of the binary tree node.
        - leftChild (BinaryTreeNode) : The left child of the binary tree.
        - rightChild (BinaryTreeNode) : The right child of the binary tree.
    """
    def __init__(self, data: int):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinaryTree:
    """
    Class to represent binary tree.
    Attributes:
        - root (BinaryTreeNode) : The root node of the binary tree.
    """
    def __init__(self):
        self.root = None
    
    def createBinaryTree(self, data: int) -> None:
        """
        Create a brand new binary tree with the data.
        Args:
            data: The value of the Binary tree node. In this case it is `int`.
        """
        self.root = BinaryTreeNode(data)
        print("Binary tree created successfully.")


# TESTING THE CLASS
bt = BinaryTree()
bt.createBinaryTree(10)
print(bt.root.data)
