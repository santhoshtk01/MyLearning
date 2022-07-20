# Program to implement deletion of the linked list

class Node:
    def __init__(self, value):
        """A node represents the value and reference of the next node"""
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def deleteNode(self, location):
        """Delete the node based on the given location"""

        # If the linked list doesn't exist
        if self.head is None:
            return "The linked list does not exist"

        # Deletion at the beginning of the linked list
        if location == 0:
            # One node linked list
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

        # Deletion at the end of the linked list
        elif location == -1:
            # One node linked list
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node.next.next is not None:
                    node = node.next

                # Actual deletion process
                node.next = None
                self.tail = node

        # Deletion at the given location
        else:
            node = self.head
            index = 0
            while index < location - 1:
                node = node.next

            # Actual deletion process
            nextNode = node.next.next
            node.next = nextNode

    def traverse(self):
        """Traverse through the linked list and prints out each nodes value"""
        if self.head is None:
            return "The linked list does not exist.."
        else:
            node = self.head
            while node.next is not None:
                print(node.value, end=" ")
                node = node.next

            # Process last node
            print(node.value)

    def deleteEntireSLL(self):
        """Delete the entire linked list"""
        if self.head is None:
            print('The linked list does not exist..')
        else:
            self.head = None
            self.tail = None


ll = SinglyLinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

ll.head = n1
n1.next = n2
n2.next = n3
n3.next = n4

ll.traverse()

ll.deleteEntireSLL()

print(ll.traverse())
