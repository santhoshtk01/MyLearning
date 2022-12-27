# Program to insert a node into the binary search tree.
from creation import BinarySearchTree, BSTNode


class BinarySearchTreeInsertion(BinarySearchTree):

    def insertNode(self, value: int):
        """
        NOTE : This is iterative approach. We can also perform recursion.

        Insert a new Binary search tree node at the vacant place.
        Args:
            value: The value of the binary search tree node.
        """
        currentNode = self.root

        while True:
            if currentNode is None:
                currentNode = BSTNode(value)
            elif currentNode.value >= value:
                if currentNode.leftChild is None:
                    currentNode.leftChild = BSTNode(value)
                    break
                else:
                    currentNode = currentNode.leftChild
            else:
                if currentNode.rightChild is None:
                    currentNode.rightChild = BSTNode(value)
                    break
                else:
                    currentNode = currentNode.rightChild


if __name__ == "__main__":
    bt = BinarySearchTreeInsertion(10)

    from random import randint

    for _ in range(5):
        bt.insertNode(randint(100, 1000))

    bt.insertNode(101010)
