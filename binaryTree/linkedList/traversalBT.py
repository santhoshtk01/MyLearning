# Program for different kind of traversal in Binary Tree.
"""
1. Preorder traversal - 'root' -> left -> right
2. Inorder traversal  - left -> 'root' -> right
3. Postorder traversal- left -> right -> 'root'
"""
from queueDs.dynamicQueue import DynamicQueue


class BinaryTreeNode:
    """
    Class to represent the binary tree node.
    Attributes:
        - data (int) : The value of the binary tree node. In this case `int`.
        - leftChild (BinaryTreeNode) : The left child of the binary tree node.
        - rightChild (BinaryTreeNode) : The right child of the binary tree node.
    """
    def __init__(self, data: int):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinaryTree:
    """
    Class to represent binary tree and its traversal techniques.
    Attributes:
        - root (BinaryTreeNode) : The root node of the binary tree.
    """
    def __init__(self):
        self.root = None

    def createBinaryTree(self, data: int):
        self.root = BinaryTreeNode(data)
        print("Binary tree created successfully.")

    def preOrderTraversal(self, rootNode):
        """Performs preorder traversal in the binary tree and print the data of the node."""
        if not rootNode:
            return
        else:
            print(rootNode.data, end=" ")
            self.preOrderTraversal(rootNode.leftChild)
            self.preOrderTraversal(rootNode.rightChild)

    def inOrderTraversal(self, rootNode, result):
        """Performs inorder traversal in the binary tree and print the data of the node."""
        result = result
        if not rootNode:
            return
        else:
            self.inOrderTraversal(rootNode.leftChild, result)
            result.append(rootNode.data)
            self.inOrderTraversal(rootNode.rightChild, result)

        return result

    def postOrderTraversal(self, rootNode):
        """Performs postorder traversal in the binary tree and print the data of the node."""
        if not rootNode:
            return
        else:
            self.postOrderTraversal(rootNode.leftChild)
            self.postOrderTraversal(rootNode.rightChild)
            print(rootNode.data, end=" ")

    def levelOrderTraversal(self):
        """Performs level order traversal and print the node in the tree level by level."""
        if not self.root:
            return "The binary tree is Empty."
        else:
            auxQueue = DynamicQueue()
            auxQueue.enQueue(self.root)

            while not auxQueue.isEmpty():
                currentNode = auxQueue.deQueue()
                print(currentNode.data, end=" ")

                if currentNode.leftChild is not None:
                    auxQueue.enQueue(currentNode.leftChild)

                if currentNode.rightChild is not None:
                    auxQueue.enQueue(currentNode.rightChild)


if __name__ == "__main__":
    pass

