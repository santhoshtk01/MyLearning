# Program for Circular doubly linked list..
# LEAVE : Tested everything and all methods are working finee..
from typing import Union


class Node:
    """A node class for circular doubly linked list.."""
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class CDoublyLinkedList:
    """A class for circular doubly linked list.."""
    def __init__(self):
        self.head = None
        self.tail = None

    def createCDLL(self, value):
        """Creates a brand new circular singly linked list.."""
        newNode = Node(value)
        newNode.next = newNode.prev = newNode
        self.head = self.tail = newNode
        print("A brand new linked list created with value {}".format(value))

    def insertNode(self, value, location: int):
        """Insert a new node at the given location.."""
        if self.head is None:
            print("The linked list does not exist..")
            self.createCDLL(value)
        else:
            newNode = Node(value)

            if location == 0:
                newNode.next = self.head
                self.head.prev = newNode
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head = newNode
            elif location == -1:
                newNode.prev = self.tail
                self.tail.next = newNode
                newNode.next = self.head
                self.head.prev = newNode
                self.tail = newNode
            else:
                index = 0
                trackNode = self.head

                while index < location - 1:
                    trackNode = trackNode.next
                    index += 1

                nextNode = trackNode.next
                trackNode.next = newNode
                newNode.prev = trackNode
                newNode.next = nextNode
                nextNode.prev = newNode

    def deleteNode(self, location: int):
        """Deletes the node at the given location.."""
        if self.head is None:
            return "The linked list does not exist.."
        else:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                if location == 0:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
                elif location == -1:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                else:
                    index = 0
                    trackNode = self.head
                    while index < location - 1:
                        index += 1
                        trackNode = trackNode.next
                    nextNode = trackNode.next.next
                    trackNode.next = nextNode
                    nextNode.prev = trackNode

    def traverse(self):
        """Traverse through the linked list and prints out the value of each node.."""
        node = self.head
        while node:
            print(node.value)
            node = node.next
            if node == self.head:
                break

    def searchNode(self, value) -> Union[int, str]:
        """Search for the node in the linked list and return the position of the node.."""
        node = self.head
        position = 0
        while node:
            if node.value == value:
                return position
            position += 1
            node = node.next
            if node == self.head:
                break
        return "The requested value does not exist in the linked list.."

    def reverseTraverse(self):
        """Reverse traverse the linked list and prints out value of each node.."""
        node = self.tail
        while node:
            print(node.value)
            node = node.prev
            if node == self.tail:
                break


# TESTING THE CIRCULAR DOUBLY LINKED LIST..
cdll = CDoublyLinkedList()
cdll.createCDLL(10)
cdll.insertNode(100, 0)
cdll.insertNode(1000, 0)
cdll.insertNode(9, -1)
cdll.insertNode(8, -1)
# [1000, 100, 10, 9, 8]
cdll.traverse()
cdll.reverseTraverse()
print(cdll.searchNode(1000))
print(cdll.searchNode(3000))

cdll.deleteNode(0)
cdll.deleteNode(-1)
cdll.deleteNode(1)

cdll.traverse()






















