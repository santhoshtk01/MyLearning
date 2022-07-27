# Program to implement insertion method for Doubly linked list


class Node:
    """A node class for doubly linked list.."""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """A class for doubly linked list.."""
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, value):
        """Creates a Doubly linked list.."""
        node = Node(value)
        self.head = self.tail = node

    def insertNode(self, value, location: int):
        """Creates a new node and Insert It at the appropriate location.."""
        if self.head is None:
            return "The linked list does not exist.."
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode

            elif location == -1:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
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


# Code to chek my function
dll = DoublyLinkedList()
dll.createDLL(10)
dll.insertNode(20, 0)
dll.insertNode(50, -1)
dll.insertNode(40, 2)
# Expected output: 20, 10, 40, 50
for value in dll:
    print(value.value, end=' ')
