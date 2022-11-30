# Complete implementation of linked list and its operations

class Node:
    """A node represents a value and reference of the next node."""
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    """A singly linked list with head and tail"""
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self, value, location: int) -> None:
        """Creates a new node and insert the node in the given location"""

        # Creating new node with the `value`
        newNode = Node(value)

        # If the node is empty
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            # At the beginning of the linked list
            if location == 0:
                newNode.next = self.head
                self.head = newNode

            # At the end of the linked list
            elif location == -1:
                self.tail.next = newNode
                self.tail = newNode

            # At any given location
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                # Actual insertion process
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def searchNode(self, value):
        """Search the given value in the linked list and return the value.."""

        # TODO : Test this with the last value of the node [Test Failed].
        #  Make the function to search the last node.

        if self.head is None:
            return "The linked list does not exist."
        else:
            node = self.head
            while node.next is not None:
                if node.value == value:
                    return node.value
                node = node.next

            return "The requested value does not exist."

    def traverse(self):
        """Traverse through the linked list and prints out all the value in each node"""

        if self.head is None:
            return "The linked list does not exist.."
        else:
            node = self.head
            while node.next is not None:
                print(node.value, end=" -> ")
                node = node.next
            # Process the last node
            print(node.value)

    def deleteNode(self, location):
        """Delete the node in the given location if it exist.."""

        if self.head is None:
            return "The linked list does not exist.."
        else:
            # At the beginning of the linked list
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next

            # At the end of the linked list

            # TODO: Check if this section handles various situation or not.

            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node.next.next is not None:
                        node = node.next
                    # Actual deletion process
                    node.next = None
                    self.tail = node
            
            # At any given location
            else:
                node = self.head
                index = 0
                while index < location - 1:
                    node = node.next
                    index += 1
                # Actual deletion process
                nextNode = node.next.next
                node.next = nextNode

    def deleteEntireList(self):
        """Delete all the nodes inside the linked list"""
        if self.head is None:
            return "The linked list does not exist.."
        else:
            self.head = None
            self.tail = None

    def detectLoop(self):
        slowPointer = self.head
        fastPointer = self.head
        f = False

        flag = slowPointer and fastPointer

        while flag and fastPointer.next.next:
            if slowPointer == fastPointer and f:
                return "Loop detected"

            # Updating the pointer
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            f = True

        return "There is no loop in the linked list.."

    def swapNode(self):
        currentNode = self.head.next
        prevNode = self.head

        while currentNode.next and prevNode.next:
            currentNode.next = prevNode
            prevNode.next = currentNode.next.next

            if prevNode == self.head:
                self.head = currentNode

            # Updating the references.
            currentNode = currentNode.next
            prevNode = prevNode.next
            break


# # Code to check my function
# ll = SinglyLinkedList()
#
# # Expected : 900 -> 30 -> 20 -> 10 -> 1000 -> 200 [😀]
# ll.insertNode(10, -1)
# ll.insertNode(20, 0)
# ll.insertNode(1000, -1)
# ll.insertNode(900, 0)
# ll.insertNode(200, -1)
# ll.insertNode(30, 1)
#
# # # Traversal [😀]
# ll.traverse()
# ll.swapNode()
# ll.traverse()
# # ll.tail.next = ll.head



# # Searching [😀]
# print(ll.searchNode(1000))
# print(ll.searchNode(30))
# print(ll.searchNode(20))
# # print(ll.searchNode(200))
#
# # Deletion of node - 30 20 1000 [😀]
# ll.deleteNode(3)
# ll.deleteNode(0)
# ll.deleteNode(-1)
# ll.traverse()
#
# # Deletion of entire linked list [😀]
# ll.deleteEntireList()
# print(ll.traverse())
