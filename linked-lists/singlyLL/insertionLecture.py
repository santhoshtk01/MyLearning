# Inserting a new node in a Singly Linked List
# 1. Create a node with value and reference
# 2. Link the node


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class singlyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self, value, location: int = None):
        """
        Insert a node in the given location.
        Args:
            value: value of the node.
            location: Reference (Physical address) of the next node.

        """
        node = Node(value)

        # If the LL is empty
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            # Insertion in beginning.
            if location == 0:
                node.next = self.head
                self.head = node

            # Insertion at the end.
            elif location == -1:
                self.tail.next = node
                self.tail = node

            # Insertion at mid of the LL.
            else:
                # TODO : Complete insertion a node in between a Linked List.
                #  the insertion happening temporarily make it permanent to the original list.
                tempNode = self.head
                index = 0
                while index <= location:
                    nextNode = tempNode.next
                    tempNode.next = node
                    node.next = nextNode

                    tempNode = tempNode.next
                    index += 1

    def printLL(self):
        """Iterate through the Linked list and return a list of values."""
        llValues = []
        tempNode = self.head

        while tempNode.next is not None:
            llValues.append(tempNode.value)
            tempNode = tempNode.next
        # Adding final value to the list `ll`
        llValues.append(tempNode.value)

        return llValues


# Checking the SinglyLL class
ll = singlyLL()
ll.insertNode(10)
ll.insertNode(20, -1)
ll.insertNode(100, 0)
ll.insertNode(1000, 1)
ll.insertNode(90, 2)

print(ll.printLL())
