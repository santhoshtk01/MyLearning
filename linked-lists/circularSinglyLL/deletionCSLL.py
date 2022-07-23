# Program to implement deletion in circular linked list..

class Node:
    """A node class with value and reference to the next node.."""
    def __init__(self, value=0, adjacent=None):
        self.value = value
        self.adjacent = adjacent


class CSinglyLinkedList:
    """A linked list with head and tail.."""
    def __init__(self):
        self.head = None
        self.tail = None

    def createCSLL(self, value):
        node = Node(value)
        node.adjacent = node
        self.head = self.tail = node

    def deleteNode(self, location: int):
        """Delete a node at the specified location.."""
        if self.head is None:
            return "The linked list does not exist.."
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.adjacent = None
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.adjacent = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.adjacent = None
                    self.head = self.tail = None
                else:
                    node = self.head
                    while node:
                        if node.adjacent.adjacent == self.head:
                            break
                        node = node.adjacent
                        node.adjacent = self.head
                        self.tail = node
            else:
                node = self.head
                index = 0
                while index < location - 1:
                    node = node.adjacent
                nextNode = node.adjacent.next
                node.adjacent = nextNode

