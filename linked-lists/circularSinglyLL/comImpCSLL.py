# Program for complete implementation of circular linked list..


class Node:
    """A node class with a value and reference of the next node.."""
    def __init__(self, value=0, adjacent=None):
        self.value = value
        self.next = adjacent


class CSinglyLinkedList:
    """A linked list with head and tail.."""
    def __init__(self):
        self.head = None
        self.tail = None

    def createCSLL(self, value) -> str:
        """Create a circular linked list with the value.."""
        if self.head:
            return "The linked list already exist.."
        else:
            node = Node(value)
            node.next = node
            self.head = self.tail = node

    def insertNode(self, value, location):
        """Creates a node and insert the node at the specified location.."""
        if self.head is None:
            return "The linked list doesn't exist.."
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head.next
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                self.tail.next = newNode
                self.tail = newNode
            else:
                node = self.head
                index = 0

                while index < location - 1:
                    node = node.next
                nextNode = node.next
                node.next = newNode
                newNode.next = nextNode

    def traverse(self):
        """Traverse the each node and prints out the value of the node.."""
        if self.head is None:
            return "The linked list does not exist.."
        else:
            node = self.head
            while node:
                print(node.value, end=' ')
                if node.next == self.head:
                    break
                node = node.next
            print()

    def searchNode(self, value):
        """Searches for a node in the linked list and return the value.."""
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

    def deleteNode(self, location):
        """Delete the node at the specified location if it exist.."""
        if self.head is None:
            return "The linked list does not exist.."
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = self.tail = None
                else:
                    node = self.head
                    while node:
                        if node.next.next == self.head:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                node = self.head
                index = 0
                while index < location - 1:
                    node = node.next
                nextNode = node.next.next
                node.next = nextNode

    def deleteEntireCSLL(self):
        """Deletes the entire linked list.."""
        self.tail.next = None
        self.head = self.tail = None


csll = CSinglyLinkedList()
csll.createCSLL(10)
csll.insertNode(1, 0)
csll.insertNode(100, -1)
csll.insertNode(5, 1)

csll.traverse()
# Expected Output - 1, 5, 10, 100 [😃]

print(csll.searchNode(1))
print(csll.searchNode(100))
print(csll.searchNode(5))
# Expected Output
# 1
# 100
# 5


csll.deleteNode(0)
csll.deleteNode(-1)
csll.deleteNode(1)

csll.traverse()
# Expected Output - 5

csll.deleteEntireCSLL()
print(csll.traverse())
