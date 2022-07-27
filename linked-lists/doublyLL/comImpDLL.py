# Program for complete implementation of doubly linked list..
from __future__ import annotations


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

    def createDLL(self, value) -> str:
        if self.head is None:
            node = Node(value)
            self.head = self.tail = node
            return "Brand new doubly linked list has been created successfully.."
        else:
            return "The doubly linked list already exist.."

    def insertNode(self, value, location: int) -> str:
        if self.head is None:
            return "The linked list does not exist.."
        else:
            newNode = Node(value)
            if location == 0:
                self.head.prev = newNode
                newNode.next = self.head
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

        return "The node has been inserted successfully.."

    def traverse(self) -> str:
        if self.head is None:
            return "The linked list does not exist.."
        else:
            node = self.head
            while node:
                print(node.value, end=' ')
                node = node.next
        print()

    def reverseTraversal(self) -> str:
        if self.head is None:
            return "The linked list does not exist.."
        else:
            node = self.tail
            while node:
                print(node.value, end=' ')
                print()
                node = node.prev

    def searchNode(self, value) -> str | object:
        if self.head is None:
            return "The linked list does not exist.."
        else:
            node = self.head
            while node:
                if node.value == value:
                    return node.value
                node = node.next
            # TODO : I am raising exception below..
            raise "ValueError"

    def deleteNode(self, location) -> str:
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
                if self.head == self.tail:
                    self.head = self.tail = None
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

    def deleteEntireDLL(self):
        if self.head is None:
            return "The linked list does not exist.."
        else:
            for node in self:
                node.prev = None
            self.head = self.tail = None

            return "The entire linked list has been deleted successfully.."


# Code to check my class
dll = DoublyLinkedList()
dll.createDLL(10)
dll.insertNode(5, 0)
dll.insertNode(20, -1)
dll.insertNode(15, 2)
dll.insertNode(100, 0)

dll.traverse()
dll.reverseTraversal()

print("=" * 10 + "Searching" + "=" * 10)
print(dll.searchNode(20))
print(dll.searchNode(5))
print(dll.searchNode(15))

# dll.deleteNode(0)
# dll.deleteNode(-1)
# dll.deleteNode(1)
#
# dll.traverse()

dll.deleteEntireDLL()
print(dll.traverse())
