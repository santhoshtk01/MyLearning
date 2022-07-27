# Program to implement the deletion method for Doubly linked list..


class Node:
    """A node class for Doubly linked list.."""
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
        """Creates a brand new doubly linked list.."""
        if self.head is None:
            node = Node(value)
            self.head = self.tail = node
        else:
            return "The linked list already exist.."

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

    def deleteNode(self, location):
        """Deletes the node at the specified location.."""
        if self.head is None:
            return "The linked list does not exist.."
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head is None:
                    return "The linked list does not exist.."
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                node = self.head
                index = 0
                while index < location - 1:
                    node = node.next
                    index += 1
                nextNode = node.next.next
                node.next = nextNode
                nextNode.prev = node

    def traverse(self):
        """Traverse the linked list and prints out the value of each node.."""
        if self.head is None:
            return "The linked list does not exist.."
        else:
            node = self.head
            while node:
                print(node.value, end=' ')
                node = node.next


# Code to check my function
dll = DoublyLinkedList()
dll.createDLL(10)
dll.insertNode(5, 0)
dll.insertNode(20, -1)
dll.insertNode(15, 2)

dll.traverse()

dll.deleteNode(0)
dll.deleteNode(1)
dll.deleteNode(-1)
print()

dll.traverse()
