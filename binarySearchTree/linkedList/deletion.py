# Program to delete a node from the Binary Search Tree.
from traversal import BinarySearchTreeTraversal
from creation import BSTNode


class BinarySearchTreeDeletion(BinarySearchTreeTraversal):
	"""Class to perform deletion of a node in binary search tree."""

	def deleteNode(self, rootNode: BSTNode, value: int) -> str:
		"""
		Delete the node which contains the given 'value' in the Binary search tree node.
		Args:
			- value (int) : The value of the binary search tree.
		Returns:
			- A meaningful message to the user of the program.
		"""
		if not rootNode:
			return

		if rootNode.value > value:
			rootNode.rightChild = self.deleteNode(rootNode.rightChild, value)
		elif rootNode.value < value:
			rootNode.leftChild = self.deleteNode(rootNode.leftChild, value)
		else:
			pass

		# TODO : Complete the deletion node.
		#  Try to understand the deletion process.





if __name__ == "__main__":
	bst = BinarySearchTreeDeletion(10)

	from random import randint
	for _ in range(5):
		bst.insertNode(randint(100, 1000))

	print(bst.preOrderTraversal())

