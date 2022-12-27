# Program to implement Binary Search Tree using Python list.


class BinarySearchTree:
    """Class to implement BST using python's list."""
    def __init__(self, size: int):
        self.tree = [None] * size
        self.lastUsedValue = 0
        self.size = size

    def insert(self, value: int) -> str:
        """
        Insert the given value at the correct position.
        Args:
            value: The value to be inserted in this case `int`.
        Returns: A meaningful message to the user of the program.
        """
        if self.lastUsedValue == self.size - 1:
            return "The tree is full."
        else:
            currentPosition = 1

            while True:
                if self.tree[currentPosition] < value:
                    currentPosition = currentPosition * 2
                else:
                    currentPosition = (currentPosition * 2) + 1

                # Check if the position is Empty if so insert the value.
                if self.tree[currentPosition * 2] is None and self.tree[currentPosition] < value:
                    self.tree[currentPosition * 2] = value
                    break
                else:
                    pass

