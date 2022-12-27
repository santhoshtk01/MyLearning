from insertion import BinaryTreeInsertion, BinaryTreeNode
from typing import Union
from queueDs.dynamicQueue import DynamicQueue


class BinaryTreeDeletion(BinaryTreeInsertion):

    def deleteNode(self, value: int) -> str:
        """Delete the Binary tree node that contains the 'value'."""
        toDelete = self.replaceValue(value)

        if not self.root:
            return "The binary tree is Empty"
        else:
            auxQueue = DynamicQueue()
            auxQueue.enQueue(self.root)

            while not auxQueue.isEmpty():
                currentNode = auxQueue.deQueue()

                if currentNode.leftChild == toDelete:
                    currentNode.leftChild = None
                    break
                else:
                    auxQueue.enQueue(currentNode.leftChild)

                if currentNode.rightChild == toDelete:
                    currentNode.rightChild = None
                    break
                else:
                    auxQueue.enQueue(currentNode.rightChild)
            else:
                return "Node not deleted from the tree."

        return "Node deleted successfully."

    def findDeepestNode(self) -> Union[BinaryTreeNode, str]:
        """Return the deepest node in the binary tree."""
        if not self.root:
            return "The binary tree is Empty."
        else:
            auxQueue = DynamicQueue()
            auxQueue.enQueue(self.root)
            lastNode = None

            while not auxQueue.isEmpty():
                currentNode = auxQueue.deQueue()
                lastNode = currentNode

                if currentNode.leftChild is not None:
                    auxQueue.enQueue(currentNode.leftChild)

                if currentNode.rightChild is not None:
                    auxQueue.enQueue(currentNode.rightChild)

            return lastNode

    def replaceValue(self, value: int):

        toReplace = self.findDeepestNode()

        if not self.root:
            return
        else:
            auxQueue = DynamicQueue()
            auxQueue.enQueue(self.root)

            while not auxQueue.isEmpty():
                currentNode = auxQueue.deQueue()

                if currentNode.data == value:
                    currentNode.data = toReplace.data
                    break

                if currentNode.leftChild is not None:
                    auxQueue.enQueue(currentNode.leftChild)

                if currentNode.rightChild is not None:
                    auxQueue.enQueue(currentNode.rightChild)

        return toReplace

    def deleteEntireBinaryTree(self):
        self.root.leftChild = None
        self.root.rightChild = None
        self.root = None


if __name__ == "__main__":
    bt = BinaryTreeDeletion()
    bt.createBinaryTree(10)

    from random import randint

    for _ in range(10):
        bt.insertNode(randint(100, 1000))

    bt.levelOrderTraversal()
    bt.deleteNode(10)
    print()
    bt.levelOrderTraversal()
    bt.deleteEntireBinaryTree()
    print(bt.postOrderTraversal(bt.root))
