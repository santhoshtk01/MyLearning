# Program to create Binary Tree using python list.


class BinaryTree:
    """Class to represent binary tree using python's list."""
    def __init__(self, size: int):
        self.binaryTree = [None] * size
        self.size = size
        self.lastUsedIndex = 0

        print("Binary tree created successfully with {} size.".format(self.size))


if __name__ == "__main__":
    bt = BinaryTree(10)
