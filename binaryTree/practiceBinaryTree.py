# Program to create a binary tree.
from stack.dynamicStack import DynamicStack
from queueDs.dynamicQueue import DynamicQueue
from typing import Union
from binaryTree.linkedList import traversalBT


class TreeNode:
    """
    Class to represent a tree node.
    Attributes:
        - data (int) : The data of the tree node.
        - leftChild (TreeNode) : The left reference of the tree node.
        - rightChild (TreeNode) : The right reference of the tree node.
    """
    def __init__(self, data: int):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinaryTree(traversalBT.BinaryTree):
    def __init__(self):
        self.root = None

    def preOrderTraversal(self):
        if not self.root:
            return "The Binary Tree is Empty.."
        else:
            auxiliaryStack = DynamicStack()
            auxiliaryStack.push(self.root)

            while not auxiliaryStack.isEmpty():
                currentNode = auxiliaryStack.pop()
                print(currentNode.data, end=" ")

                if currentNode.rightChild is not None:
                    auxiliaryStack.push(currentNode.rightChild)

                if currentNode.leftChild is not None:
                    auxiliaryStack.push(currentNode.leftChild)
        print()
    #
    # def inOrderTraversal(self):
    #     pass
    #
    # def postOrderTraversal(self):
    #     pass

    def levelOrderTraversal(self):
        """Traverse through the binary tree level by level."""
        if not self.root:
            return "The Binary Tree is Empty."
        else:
            auxiliaryQueue = DynamicQueue()
            auxiliaryQueue.enQueue(self.root)

            while not auxiliaryQueue.isEmpty():
                currentNode = auxiliaryQueue.deQueue()
                print(currentNode.data, end=" ")

                if currentNode.leftChild is not None:
                    auxiliaryQueue.enQueue(currentNode.leftChild)

                if currentNode.rightChild is not None:
                    auxiliaryQueue.enQueue(currentNode.rightChild)
        print()

    def isContains(self, value: int) -> Union[str, bool]:
        """Return 'True' if the value found in the Binary Tree. Otherwise, return 'False'."""
        if not self.root:
            return "The Binary Tree is Empty.."
        else:
            auxiliaryQueue = DynamicQueue()
            auxiliaryQueue.enQueue(self.root)

            while not auxiliaryQueue.isEmpty():
                currentNode = auxiliaryQueue.deQueue()

                # Check if exist
                if currentNode.data == value:
                    return True

                # Updating the queue to further nodes in the tree.
                if currentNode.leftChild is not None:
                    auxiliaryQueue.enQueue(currentNode.leftChild)

                if currentNode.rightChild is not None:
                    auxiliaryQueue.enQueue(currentNode.rightChild)

        return False

    def insertNode(self, value: int) -> str:
        """
        Insert the Binary Tree Node at the vacant place.
        Args:
            value: The value of the Binary tree Node.
        """
        if not self.root:
            return "The Binary Tree is Empty."
        else:
            auxiliaryQueue = DynamicQueue()
            auxiliaryQueue.enQueue(self.root)

            while not auxiliaryQueue.isEmpty():
                currentNode = auxiliaryQueue.deQueue()

                # Check if the node has vacant.
                if currentNode.leftChild is None:
                    currentNode.leftChild = TreeNode(value)
                    return "The node inserted at leftChild of {} Successfully.".format(currentNode.data)

                elif currentNode.rightChild is None:
                    currentNode.rightChild = TreeNode(value)
                    return "The node inserted at rightChild of {} successfully.".format(currentNode.data)

                # Adding the further node to the queue.
                if currentNode.leftChild is not None:
                    auxiliaryQueue.enQueue(currentNode.leftChild)

                if currentNode.rightChild is not None:
                    auxiliaryQueue.enQueue(currentNode.rightChild)

    def getDeepestNode(self) -> Union[TreeNode, str]:
        """Return the deepest node (last Node) in the Binary Tree."""
        if not self.root:
            return "The Binary Tree is Empty."
        else:
            auxiliaryQueue = DynamicQueue()
            auxiliaryQueue.enQueue(self.root)
            lastNode = None

            while not auxiliaryQueue.isEmpty():
                lastNode = auxiliaryQueue.deQueue()

                if lastNode.leftChild is not None:
                    auxiliaryQueue.enQueue(lastNode.leftChild)

                if lastNode.rightChild is not None:
                    auxiliaryQueue.enQueue(lastNode.rightChild)

            return lastNode

    def __deleteDeepestNode(self) -> Union[int, str]:
        """
        Delete the deepest node return by the `getDeepestNode` method. Return the
        data of the deleted node.
        """
        toDelete = self.getDeepestNode()
        value = toDelete.data

        if not self.root:
            return "The Binary tree is Empty."
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

            return value

    def deleteNode(self, value: int) -> str:
        """
        Delete the Tree node that contains the 'value'.
        Args:
            value: The data or value of the tree node.

        Returns: A meaningful message to the user of the program.
        """
        toReplace = self.__deleteDeepestNode()

        if not self.root:
            return "The Binary tree is Empty."
        else:
            auxQueue = DynamicQueue()
            auxQueue.enQueue(self.root)

            while not auxQueue.isEmpty():
                currentNode = auxQueue.deQueue()

                # Replace the value of the Binary Tree Node.
                if currentNode.data == value:
                    currentNode.data = toReplace
                    break

                # Visiting the further nodes.
                if currentNode.leftChild is not None:
                    auxQueue.enQueue(currentNode.leftChild)

                if currentNode.rightChild is not None:
                    auxQueue.enQueue(currentNode.rightChild)



def main():
    # Creating a binary tree
    b = BinaryTree()
    b.root = TreeNode(10)
    b.root.leftChild = TreeNode(20)
    b.root.rightChild = TreeNode(30)
    """
        10
       /  \
      20  30
     /  \
    40  50
    """
    b.root.leftChild.leftChild = TreeNode(40)
    b.root.leftChild.rightChild = TreeNode(50)

    b.preOrderTraversal(b.root)  # 10 20 40 50 30
    print(b.inOrderTraversal(b.root, []))
    b.postOrderTraversal(b.root)
    print(b.inOrderTraversal(b.root, []))
    b.levelOrderTraversal()



if __name__ == "__main__":
    main()
