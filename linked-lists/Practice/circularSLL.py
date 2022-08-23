# Program for circular singly linked list..
from typing import Union

class Node:
    """A node class for circular singly linked list.."""
    def __init__(self, value):
        self.value = value
        self.next = None


class CSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def getLastNode(self):
        """Returns the last node in the circular singly linked list.."""
        trackNode = self.head
        flag = True
        while trackNode != self.tail or flag:
            flag = False
            trackNode = trackNode.next

        return trackNode

    def createCSLL(self, value):
        """Creates a brand new circular singly linked list.."""
        newNode = Node(value)
        self.head = self.tail = newNode
        newNode.next = newNode
        print("Brand new linked list created with value {}".format(value))

    def insertNode(self, value, location: int):
        """Insert a new node @ the specified location.."""
        if self.head is None:
            print("The linked list doesn't exist..")
            self.createCSLL(value)
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = self.head
            elif location == -1:
                node = self.getLastNode()
                node.next = newNode
                newNode.next = self.head
                self.tail = newNode
            else:
                index = 0
                node = self.head
                while index < location - 1:
                    index += 1
                    node = node.next
                nextNode = node.next
                node.next = newNode
                newNode.next = nextNode

    def deleteNode(self, location: int):
        """Deletes a node at the given location.."""
        if self.head is None:
            return "The linked list does not exist.."
        else:
            # If it has only one node..
            if self.head == self.tail:
                self.head = self.tail = None

            # If it has more than one node..
            if location == 0:
                self.head = self.head.next
                self.tail.next = self.head
            elif location == -1:
                trackNode = self.head
                while trackNode.next.next != self.head:
                    trackNode = trackNode.next
                trackNode.next = self.head
                self.tail = trackNode
            else:
                index = 0
                trackNode = self.head
                while index < location - 1:
                    index += 1
                    trackNode = trackNode.next
                nextNode = trackNode.next.next
                trackNode.next = nextNode

    def traverse(self):
        """Traverse through the linked list and prints out each value of the node.."""
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.next
            if node == self.head:
                break
        print()

    def searchNode(self, value) -> Union[int, str]:
        """Search the value and return the position of the node.."""
        trackNode = self.head
        position = 0
        while trackNode:
            if trackNode.value == value:
                return position
            position += 1
            trackNode = trackNode.next
            if trackNode == self.head:
                break

        return "The requested value not found in the linked list.."


# TESTING THE CIRCULAR SINGLY LINKED LIST..
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
# 0
# 3
# 1


csll.deleteNode(0)
csll.deleteNode(-1)
csll.deleteNode(1)

csll.traverse()
# Expected Output - 5
















