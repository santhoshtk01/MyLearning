# Program to implement deletion method in circular doubly linked list..


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

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createCDLL(self, value):
        newNode = Node(value)
        self.head = self.tail = newNode
        newNode.next = newNode.prev = newNode

    def insertNode(self, value, location: int):
        """Insert a new node at the specified location.."""
        if self.head is None:
            return "The linked list does not exist.."
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
                self.tail = newNode
                self.tail.next = self.head
                self.head.prev = self.tail

            else:
                node = self.head
                index = 0
                while index < location - 1:
                    node = node.next
                    index += 1
                nextNode = node.next
                node.next = newNode
                newNode.prev = node
                newNode.next = nextNode
                nextNode.prev = newNode

    def deleteNode(self, location: int):
        """Deletes a node in the specified location.."""
        if self.head is None:
            return "The linked list does not exist.."
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = self.head.prev = None
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
                    self.head.prev = self.tail

            elif location == -1:
                if self.head is None:
                    self.head.next = self.tail.next = None
                    self.head = self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.head.prev = self.tail
                    self.tail.next = self.head

            else:
                index = 0
                node = self.head
                while index < location - 1:
                    node = node.next
                    index += 1

                nextNode = node.next.next
                node.next = nextNode
                nextNode.prev = node


# Code to test the class and deletion method..
cdll = CDoublyLinkedList()
cdll.createCDLL(10)
cdll.insertNode(100, 0)
cdll.insertNode(1000, 0)
cdll.insertNode(9, -1)
cdll.insertNode(8, -1)

print([node.value for node in cdll])

cdll.deleteNode(0)
cdll.deleteNode(-1)
cdll.deleteNode(1)
print([node.value for node in cdll])  # [100, 9]




















