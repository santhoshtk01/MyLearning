# Program to find the middle node in a linked list


class Node:
    """A node represents a value and the address of the next node."""
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def findLength(self):
        """Returns the length of the linked list."""
        length = 0
        node = self.head

        while node.next is not None:
            length += 1
            node = node.next
        length += 1

        return length

    def findMid(self):
        middle = self.findLength() // 2
        trackNode = self.head
        index = 0

        while index < middle:
            trackNode = trackNode.next
            index += 1

        return trackNode.value


ll = SinglyLinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

ll.head = n1
n1.next = n2
n2.next = n3


print(ll.findMid())


# Program to implement two pointer approach to find the middle of the linked list.

class Node:
    """A node represents a value and address of the next node."""
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self, value):
        """Creates a node and insert the node in the linked list."""
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def traverse(self):
        """Traverse the linked list and prints out each node value."""
        if self.head is None:
            return "The linked list does not exist."
        else:
            node = self.head
            while node.next is not None:
                print(node.value, end=" ")
                node = node.next
            # Process the last node
            print(node.value)

    def findMid(self):
        """Find the middle node of the linked list."""
        if self.head is None:
            return "The linked list does not exist."
        else:
            slowTrack = self.head
            fastTrack = self.head

            while fastTrack and fastTrack.next is not None:
                slowTrack = slowTrack.next
                fastTrack = fastTrack.next.next

            return slowTrack.value


# Code to check my function
ll = SinglyLinkedList()
for value in range(1, 15, 2):
    ll.insertNode(value)
ll.traverse()
print(ll.findMid())
