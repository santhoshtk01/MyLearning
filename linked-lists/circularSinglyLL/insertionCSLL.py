# Program to create insertion method for Circular singly linked list


class Node:
    """A node with value and reference of the next node.."""

    def __init__(self, value):
        self.value = value
        self.adjacent = None


class CSinglyLinkedList:
    """A class represents linked list with head and tail.."""

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

    def createCSLL(self, value):
        """Create a new circular list if it doesn't exist.."""
        if self.head:
            return "The linked list already exist.."
        else:
            node = Node(value)
            node.adjacent = node
            self.head = self.tail = node

    def insertNode(self, value, location):
        """Insert a new node at the specified location.."""

        newNode = Node(value)

        if self.head is None:
            return "The linked list doesn't exist.."
        else:
            # At the beginning of the linked list
            if location == 0:
                self.tail.adjacent = newNode
                newNode.adjacent = self.head
                self.head = newNode

            # At the end of the linked list
            elif location == -1:
                newNode.adjacent = self.head
                self.tail.next = newNode
                self.tail = newNode

            # At any given location
            else:
                node = self.head
                index = 0
                while index < location - 1:
                    node = node.adjacent
                    index += 1
                nextNode = node.adjacent
                node.adjacent = newNode
                newNode.adjacent = nextNode

    def traverse(self):
        """Traverse the linked list and prints out each node value.."""
        if self.head is None:
            return "The linked list does not exist.."
        else:
            node = self.head
            while node:
                print(node.value, end=" ")
                if node.next == self.head:
                    break
                node = node.next

    def searchNode(self, value):
        """Search for a value in the linked list and return the value"""
        if self.head is None:
            return "The linked list does not exist.."
        else:
            node = self.head
            while node:
                if node.value == value:
                    return node.value

                if node.next == self.head:
                    return "The requested value does not exist.."

                node = node.next


# Code to check my function
csll = CSinglyLinkedList()
csll.createCSLL(10)
csll.insertNode(20, -1)
csll.insertNode(50, -1)
csll.insertNode(30, 0)
csll.insertNode(40, 1)

# 30, 40, 10, 20, 50
for value in csll:
    print(value.value, end=' ')
