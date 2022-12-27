# Program to implement different kind of traversal in Binary Search Tree.
from insertion import BinarySearchTreeInsertion
from stack.dynamicStack import DynamicStack
from typing import Union


class BinarySearchTreeTraversal(BinarySearchTreeInsertion):
    """Class to implement binary search tree traversals in iterative approach."""

    def preOrderTraversal(self) -> Union[str, list]:
        """Performs pre-order traversal in the binary search tree and return a list."""
        result = []
        if not self.root:
            return "The binary search tree is Empty."
        else:
            auxStack = DynamicStack()
            auxStack.push(self.root)

            while not auxStack.isEmpty():
                currentNode = auxStack.pop()
                result.append(currentNode.value)

                # Processing the left child of the current node.
                if currentNode.leftChild is not None:
                    auxStack.push(currentNode.leftChild)

                # Processing the right child of the current node.
                if currentNode.rightChild is not None:
                    auxStack.push(currentNode.rightChild)

        return result

    def inOrderTraversal(self) -> Union[str, list]:
        """Performs In-Order traversal in the binary search tree and return a list."""
        result = []

        if not self.root:
            return "The Binary search tree is Empty."
        else:
            auxStack = DynamicStack()
            currentNode = self.root

            while True:
                if currentNode is not None:
                    auxStack.push(currentNode)
                    currentNode = currentNode.leftChild
                elif not auxStack.isEmpty():
                    poppedItem = auxStack.pop()
                    result.append(poppedItem.value)
                    currentNode = poppedItem.rightChild
                else:
                    break

        return result

    def postOrderTraversal(self) -> Union[str, list]:
        """Performs Post-Order traversal in the binary tree and return a list."""
        # TODO : Debug this code and make the code to return correct output.
        result = []

        auxStack1 = DynamicStack()
        auxStack2 = DynamicStack()

        auxStack1.push(self.root)

        while not auxStack1.isEmpty():
            currentNode = auxStack1.pop()
            auxStack2.push(currentNode)

            if currentNode.leftChild is not None:
                auxStack1.push(currentNode.leftChild)

            if currentNode.rightChild is not None:
                auxStack1.push(currentNode.rightChild)

        while not auxStack2.isEmpty():
            result.append(auxStack2.pop().value)

        return result

    def searchNode(self, value: int) -> Union[str, bool]:
        """
        Search for the node that contains the 'value' and return True if found.
        Otherwise, return False.
        Args:
            value: The value of the Binary search tree node.
        Returns: True if found. Otherwise, return False.
        """
        if not self.root:
            return "The binary tree is Empty."
        else:
            currentNode = self.root

            while True:
                if currentNode.value == value:
                    return True
                else:
                    if currentNode.value <= value:
                        if currentNode.rightChild is not None:
                            currentNode = currentNode.rightChild
                        else:
                            break
                    else:
                        if currentNode.leftChild is not None:
                            currentNode = currentNode.leftChild
                        else:
                            break
            return False


if __name__ == "__main__":
    bt = BinarySearchTreeTraversal(10)

    from random import randint

    for _ in range(50):
        bt.insertNode(randint(1, 200))

    print(bt.preOrderTraversal())
    print(bt.inOrderTraversal())
    print(bt.postOrderTraversal())
    print(bt.searchNode(36))

