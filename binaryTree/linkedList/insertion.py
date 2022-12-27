# Program to insert nodes in binary tree.
from queueDs.dynamicQueue import DynamicQueue
from traversalBT import BinaryTree


class BinaryTreeNode:
    """Class to represent a binary tree node."""
    def __init__(self, value: int):
        self.data = value
        self.leftChild = None
        self.rightChild = None


class BinaryTreeInsertion(BinaryTree):

    def insertNode(self, value: int):
        if not self.root:
            return "The Binary tree is Empty."
        else:
            auxQueue = DynamicQueue()
            auxQueue.enQueue(self.root)

            while not auxQueue.isEmpty():
                currentNode = auxQueue.deQueue()

                # Check the left child of the tree
                if currentNode.leftChild is None:
                    currentNode.leftChild = BinaryTreeNode(value)
                    break
                else:
                    auxQueue.enQueue(currentNode.leftChild)

                # Check the right child of the tree
                if currentNode.rightChild is None:
                    currentNode.rightChild = BinaryTreeNode(value)
                    break
                else:
                    auxQueue.enQueue(currentNode.rightChild)


if __name__ == "__main__":
    bt = BinaryTreeInsertion()
    bt.createBinaryTree(10)

    bt.insertNode(20)
    bt.insertNode(30)
    bt.insertNode(40)
    bt.insertNode(50)

    bt.levelOrderTraversal()
    print()
    bt.preOrderTraversal(bt.root)
    print()
    bt.postOrderTraversal(bt.root)

