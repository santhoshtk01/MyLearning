# Program to create Doubly linked list


class Node:
    """A node class for doubly linked list.."""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """A class to create doubly linked list.."""
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, value):
        """Create a doubly linked list with the specified value.."""
        node = Node(value)
        self.head = self.tail = node


# Code to check my class
dll = DoublyLinkedList()
dll.createDLL(10)
print([val.value for val in dll])
