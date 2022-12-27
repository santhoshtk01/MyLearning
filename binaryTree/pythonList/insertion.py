# Program to insert a new node (value) to Binary tree(List).
from creation import BinaryTree


class BinaryTreeInsertion(BinaryTree):

    def insertNode(self, value: int) -> str:
        """Insert a new value at the vacant place in the binary tree."""
        if self.lastUsedIndex + 1 == self.size:
            return "There is no more place to insert a new value."
        else:
            self.binaryTree[self.lastUsedIndex + 1] = value
            self.lastUsedIndex += 1

            return "The value inserted successfully."


if __name__ == "__main__":
    bt = BinaryTreeInsertion(10)

    from random import randint

    # NOTE : The zero index is always skipped to make mathematical computation easier.
    for _ in range(10):
        print(bt.insertNode(randint(1000, 10_000)))

    print(bt.insertNode(100))

