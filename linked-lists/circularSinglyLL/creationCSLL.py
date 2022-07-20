# Program to creation of Circular singly linked list


class Node:
    """A node represents a value and the reference of the next node."""
    def __init__(self, value):
        self.value = value
        self.next = None


class CSinglyLinkedList:
    """A linked list with head and tail."""
    def __init__(self):
        self.head = None
        self.tail = None

    def createCSLL(self, value):
        node = Node(value)
        self.head = self.tail = node
        node.next = node

    def __iter__(self):
        node = self.head
        while node.next != self.head:
            yield node.value
        node = node.next
        yield node.value


# Code to check my function
csll = CSinglyLinkedList()
csll.createCSLL(10)

for value in csll:
    print(value)

