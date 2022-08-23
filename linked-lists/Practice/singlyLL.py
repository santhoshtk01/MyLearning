# Program for Linked list practice


class Node:
    """A node class for linked list.."""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """A class for linked list with all functionality. Each functionality is carried out by a method."""

    def __init__(self):
        self.head = None
        self.tail = None

    def createLL(self, value):
        """Creates a brand new singly linked list.."""
        print("Creating....")
        newNode = Node(value)
        self.head = self.tail = newNode

    def insertNode(self, value, location: int):
        """Insert a new node at the specified location.."""
        print("Inserting....")
        if self.head is None:
            print("The linked list does not exist..")
            # value = input('Enter a value to create one: ')
            #
            # # Convert to int if Integer
            # try:
            #     value = int(value)
            # except ValueError:
            #     pass
            self.createLL(value)
            print("Brand new Linked list created successfully with value {}".format(value))
        else:
            newNode = Node(value)

            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                self.tail.next = newNode
                self.tail = newNode
            else:
                trackNode = self.head
                index = 0

                while index < location - 1:
                    trackNode = trackNode.next
                    index += 1

                nextNode = trackNode.next
                trackNode.next = newNode
                newNode.next = nextNode

    def deleteNode(self, location: int):
        """Deletes a node at the given location.."""
        print("Deleting....")
        if self.head is None:
            return "The linked list does not exist.."
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    node = self.head
                    while node:
                        if node.next.next is None:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                trackNode = self.head
                index = 0
                while index < location - 1:
                    trackNode = trackNode.next
                    index += 1
                trackNode.next = trackNode.next.next

    def traverse(self):
        """Traverse through the linked list and prints out the value of each node.."""
        print("Traversing....")
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def searchNode(self, value):
        """Search for the value and return the position of the node.."""
        print("searching....")
        position = 0
        node = self.head

        while node.value != value:
            position += 1
            node = node.next

        return position


# TESTING THE LINKED LIST CLASS..
ll = LinkedList()
ll.createLL(10)
ll.insertNode(1000, 0)
ll.insertNode(2000, -1)
ll.insertNode(3000, 2)
ll.insertNode(4000, -1)
ll.insertNode(5000, -1)
# [1000, 10, 3000, 2000, 4000, 5000]
ll.traverse()
print(ll.searchNode(3000))
print(ll.searchNode(5000))

ll.deleteNode(0)
ll.deleteNode(-1)
ll.deleteNode(2)

# [10, 3000, 4000]
ll.traverse()
