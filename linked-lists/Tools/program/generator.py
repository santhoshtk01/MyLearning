# Program to generate linked list for practice.
from random import randint


class Node:
    """A class to represent the node.
    Attributes:
        - value (Any) : The value of the node.
        - next (Node) : The reference of the next Node.
    """
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    """A class to generate linked list of given length with random values. Default random values: (1, 10).
    Attributes:
        - head (Node) : The head of the linked list which means the first node.
        - tail (Node) : The tail of the linked list which means the last node.
        - length (int) : The length of the linked list.
    """
    def __init__(self, length: int):
        self.head = None
        self.tail = None
        self.length = length
        self.generateLinkedList()

    def __iter__(self):
        temp = self.head

        while temp:
            yield temp.value
            temp = temp.next

    def __str__(self):
        temp = self.head
        output = ""

        while temp:
            output += str(temp.value)
            output += " -> "
            temp = temp.next

        return output

    def generateLinkedList(self):
        """Generates a linked list with random numbers at the given range."""
        self.head = Node(10)
        temp = self.head

        for index in range(self.length):
            temp.next = Node(randint(1, 10))
            temp = temp.next

        return self.head

    def returnList(self):
        """Return node values as list."""
        return [value for value in self]

