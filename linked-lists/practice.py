# Program to create Circular singly linked list and its operations

class Node:
    """A node class with value and reference of the next node.."""
    def __init__(self, value):
        self.value = value
        self.next = None


class CSinglyLinkedList:
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
        """Create a circular singly linked list with one node.."""
        node = Node(value)
        node.next = node
        self.head = self.tail = node

    def insertNode(self, value, location):
        """Insert a new node at the specified location.."""
        if self.head is None:
            return "The linked list does not exist.."
        else:
            node = Node(value)

            # At the beginning of the linked list
            if location == 0:
                node.next = self.head
                self.head = node
                self.tail.next = node

            # At the end of the linked list
            elif location == -1:
                self.tail.next = node
                self.tail = node
                node.next = self.head

            # At the specified location
            else:
                tempNode = self.head
                index = 0

                while index < location - 1:
                    tempNode = tempNode.next

                nextNode = tempNode.next
                tempNode.next = node
                node.next = nextNode

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
csll.traverse()
print(csll.searchNode(10))
print(csll.searchNode(50))
print(csll.searchNode(40))

# 30, 40, 10, 20
for value in csll:
    print(value.value, end= ' ')



