# Program for creation of brand new circular doubly linked list..


class Node:
    """A class node for circular doubly linked list.."""

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CDoublyLinkedList:
    """A class for circular doubly linked list.."""

    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        node = self.head
        flag = True
        while node != self.head or flag:
            print(node.value, end=' ')
            node = node.next
            flag = False

    def createCDLL(self, value) -> str:
        """Creates a brand new linked list If doesn't exist.."""
        if self.head is None:
            newNode = Node(value)
            newNode.next = newNode.prev = newNode
            self.head = self.tail = newNode
        else:
            return "The linked list already exist.."

        return "The doubly linked list created successfully."

    def insertNode(self, value, location: int) -> str:
        """Creates a brand new node and insert it at the specified location.."""
        if self.head is None:
            return "The linked list does not exist.."
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.head = newNode
            elif location == -1:
                # Updating new node reference..
                newNode.prev = self.tail
                newNode.next = self.head
                # Updating head and tail reference..
                self.tail.next = newNode
                self.head.prev = newNode
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

        return "The value inserted successfully.."

    def reverseTraversal(self) -> None:
        """Traverse through the linked list in reverse order and print the value in descending order"""
        node = self.tail
        while node:
            if node.prev == self.tail:
                print(node.value)
                break
            print(node.value, end=' ')
            node = node.prev


# TESTING THE CLASS AND METHODS
cdll = CDoublyLinkedList()
cdll.createCDLL(10)
cdll.insertNode(100, 0)
cdll.insertNode(1000, 0)
cdll.insertNode(9, -1)
cdll.insertNode(8, -1)
print(cdll.insertNode("second", 2))
cdll.insertNode("third", 3)

cdll.traverse()
print()
cdll.reverseTraversal()
