# Program for doubly linked list..
# TODO : Remove the print statement for testing []


class Node:
    """A node class for doubly linked list.."""
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """A class for doubly linked list.."""
    def __init__(self):
        self.head = None
        self.tail = None

    def createDLL(self, value):
        """Creates a brand new linked list.."""
        print("Creating....")
        newNode = Node(value)
        self.head = self.tail = newNode
        print("A brand new linked list is created with the value {}".format(value))

    def insertNode(self, value, location: int):
        """Insert a new node at the given location.."""
        print("Inserting....")
        if self.head is None:
            print("The linked list does not exist..")
            self.createDLL(value)
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

    def deleteNode(self, location: int):
        """Deletes the node at the given location.."""
        print("Deleting....")
        if self.head is None:
            print("The linked list does not exist..")
        else:
            # If LL has one node..
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                # If LL has more than one node..
                if location == 0:
                    self.head = self.head.next
                    self.head.prev = None
                elif location == -1:
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
        """Traverse through the linked list and prints out value of each node.."""
        print("Traversing....")
        trackNode = self.head
        while trackNode:
            print(trackNode.value)
            trackNode = trackNode.next

    def reverseTraverse(self):
        """Reverse traverse through the linked list and prints out each node value.."""
        print("Reverse traversing....")
        trackNode = self.tail
        while trackNode:
            print(trackNode.value)
            trackNode = trackNode.prev

    def searchNode(self, value):
        """Search for the value and return the position of the node.."""
        print("Searching....")
        trackNode = self.head
        position = 0
        while trackNode:
            if trackNode.value == value:
                return position
            trackNode = trackNode.next
            position += 1

        return "The requested value does not exist in the linked list.."


# TESTING THE DOUBLY LINKED LIST CLASS..
dll = DoublyLinkedList()
dll.createDLL(10)

dll.insertNode(1000, 0)
dll.insertNode(2000, -1)
dll.insertNode(3000, 2)

# [1000, 10, 3000, 2000]
dll.traverse()
# [2000, 3000, 10, 1000]
dll.reverseTraverse()

print(dll.searchNode(1000))
print(dll.searchNode(2000))
print(dll.searchNode(10))

dll.deleteNode(0)
dll.deleteNode(1)
dll.deleteNode(-1)

# [10]
dll.traverse()
dll.deleteNode(0)
print(dll.traverse())












