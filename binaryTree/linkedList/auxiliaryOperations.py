# Program for auxiliary operations for binary tree.
from binaryTree.linkedList.insertion import BinaryTreeInsertion
from queueDs.dynamicQueue import DynamicQueue


class AuxiliaryOperations(BinaryTreeInsertion):
    """Class to implement auxiliary operations for binary tree."""

    def findMaximumValue(self):
        """Iterative approach for finding maximum value in the binary tree."""
        maxValue = float("-inf")
        if not self.root:
            return "The binary tree is Empty."
        else:
            auxQueue = DynamicQueue()
            auxQueue.enQueue(self.root)

            while not auxQueue.isEmpty():
                currentNode = auxQueue.deQueue()

                # Updating the maximum value in the tree.
                if currentNode.data > maxValue:
                    maxValue = currentNode.data

                # Updating the left child
                if currentNode.leftChild is not None:
                    auxQueue.enQueue(currentNode.leftChild)

                # Updating the right child
                if currentNode.rightChild is not None:
                    auxQueue.enQueue(currentNode.rightChild)

        return maxValue


if __name__ == "__main__":
    bt = AuxiliaryOperations()
    bt.createBinaryTree(10)

    bt.insertNode(20)
    bt.insertNode(300)
    bt.insertNode(40)
    bt.insertNode(50)

    print(bt.findMaximumValue())