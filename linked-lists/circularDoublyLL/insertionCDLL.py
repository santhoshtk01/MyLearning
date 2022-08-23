# Program for insertion in circular doubly linked list..
from typing import Union


class Node:
    """A class for node"""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CDoublyLinkedList:
    """A class Circular for doubly linked list.."""
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createCDLL(self, value):
        """Creates a brand new circular doubly linked list.."""
        if self.head is None:
            newNode = Node(value)
            self.head = self.tail = newNode
            newNode.next = newNode.prev = newNode
        else:
            return "The circular doubly linked list already exist.."

    def insertNode(self, value, location: int) -> str:
        """Insert a new node at the specified location.."""

        # If LL doesn't exist creates one..
        if self.head is None:
            self.createCDLL(value)
            return "The linked list doesn't exist so we created one for you" \
                   "with the given value {0}".format(value)
        else:
            newNode = Node(value)

            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode

            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
                self.head.prev = newNode

            else:
                trackNode = self.head
                index = 0
                while index < location - 1:
                    trackNode = trackNode.next
                    index += 1

                nextNode = trackNode.next
                trackNode.next = newNode
                newNode.prev = trackNode
                newNode.next = nextNode
                nextNode.prev = newNode
        return "The value {0} inserted successfully at the given location {1}.".format(value, location)

    def traverse(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            if node == self.tail:
                break
            node = node.next

    def searchNode(self, value) -> Union[str, object]:
        if self.head is None:
            return "The linked list doesn't exist.."
        else:
            trackNode = self.head
            while trackNode.value != value:
                if trackNode == self.tail:
                    return "The requested value does not exist.."
                trackNode = trackNode.next
            return trackNode


# TESTING THE CIRCULAR DOUBLY LINKED LIST CLASS
# =============================================
# TEST 1 - ✅
# TEST 2 - ✅

cdll = CDoublyLinkedList()
cdll.createCDLL(10)
print(cdll.insertNode(100, 0))
print(cdll.insertNode(1000, 0))
print(cdll.insertNode(9, -1))
print(cdll.insertNode(8, -1))

print([node.value for node in cdll])
print(cdll.searchNode(1000))
print(cdll.searchNode(3000))
