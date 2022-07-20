# Program to make insertion in singly linked list

class Node:
    """A node represents a value and reference to the next node"""
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    """A singly linked list contains head and tail"""
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self, value, location):
        # Creating a new node
        newNode = Node(value)

        # If the linked list is empty
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            # At the beginning of the linked list
            if location == 0:
                newNode.next = self.head
                self.head = newNode

            # At the end of the linked list
            elif location == -1:
                self.tail.next = newNode
                self.tail = newNode

            # At the middle of the linked list
            else:
                tempNode = self.head
                index = 0

                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1

                # Actual insertion
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

                # In case of last node
                if tempNode == self.tail:
                    self.tail = newNode

    def traverse(self):
        """Traverse the linked list and prints out each items value"""
        if self.head is None:
            print("The singly linked list does not exist")
        else:
            node = self.head
            while node.next is not None:
                print(node.value, end=" ")
                node = node.next
            # Prints out the last node
            print(node.value)

    def findNode(self, toFind):
        """Find the node if it exist in the linked list."""
        if self.head is None:
            return "The linked list doesn't exist."
        else:
            node = self.head
            while node.next is not None:
                if node.value == toFind:
                    return node.value
                node = node.next
            return "The value requested doesn't exist in the linked list"


# Code to check my linked list insertion method
ll = SinglyLinkedList()
ll.insertNode(10, 0)
ll.insertNode(200, -1)
ll.insertNode(1000, 1)
ll.traverse()
print(ll.findNode(200))
print(ll.findNode(1000))
print(ll.findNode(300))
