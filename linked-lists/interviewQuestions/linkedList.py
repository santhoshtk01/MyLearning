# Program to create a customized linked list class..
from random import randint


class Node:
    """A node class for customized linked list.."""

    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    """A class for customized linked list.."""
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(node.value) for node in self]
        return " -> ".join(values)

    def __len__(self):
        values = [node for node in self]
        return len(values)

    def add(self, value):
        """Add a new node at the end of the linked list with the `value`."""
        newNode = Node(value)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def generateLL(self, n, minValue, maxValue):
        """Generates a new linked list with random values between `minValue` and `maxValue`"""
        self.head = self.tail = None
        for _ in range(n):
            value = randint(minValue, maxValue)
            self.add(value)


# TESTING THE CUSTOMIZED LINKED LIST
# ll = LinkedList()
# ll.generateLL(10, 1000, 10000)
# print(ll)
# print(len(ll))







