from insertion import BinaryTreeInsertion


class BinaryTreeTraversal(BinaryTreeInsertion):

    def preOrderTraversal(self, index):
        """Root -> left -> right"""
        if index > self.lastUsedIndex:
            return
        else:
            print(self.binaryTree[index], end=" ")
            self.preOrderTraversal(index * 2)
            self.preOrderTraversal((index * 2) + 1)

    def inOrderTraversal(self, index):
        """left -> root -> right"""
        if index > self.lastUsedIndex:
            return
        else:
            self.inOrderTraversal(index * 2)
            print(self.binaryTree[index], end=" ")
            self.inOrderTraversal((index * 2) + 1)

    def postOrderTraversal(self, index):
        """left -> right -> root"""
        if index > self.lastUsedIndex:
            return
        else:
            self.postOrderTraversal(index * 2)
            self.postOrderTraversal((index * 2) + 1)
            print(self.binaryTree[index], end=" ")

    def levelOrderTraversal(self):
        for value in self.binaryTree:
            if value:
                print(value, end=" ")


if __name__ == "__main__":
    bt = BinaryTreeTraversal(10)

    from random import randint

    # NOTE : The zero index is always skipped to make mathematical computation easier.
    for _ in range(5):
        print(bt.insertNode(randint(1000, 10_000)))

    bt.preOrderTraversal(1)
    print()
    bt.inOrderTraversal(1)
    print()
    bt.postOrderTraversal(1)
    print()
    bt.levelOrderTraversal()
