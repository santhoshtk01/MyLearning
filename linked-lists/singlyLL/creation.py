# Creating the Singly Linked list in Python
# 1. Create a head and tail with none
# 2. Create a node with value and reference as none
# 3. Link the node with head and tail

class Node:
    """
    A Node in a linked list contains a value and a reference to
    the next value. NODE : [value, reference]
    """

    def __init__(self, value=None):
        self.value = value
        # Contains the next node address.
        self.next = None


class SLinkedList:
    """
    Linked list contains a Head and Tail by default. After
    creation of node we can change the reference of them.
    """

    def __init__(self):
        self.head = None
        self.tail = None


# Creating linked list
sll = SLinkedList()
node1 = Node(10)
node2 = Node(20)

sll.head = node1
sll.head.next = node2
sll.tail = node2

print(sll.head.value)  # 10
print(sll.head.next.value)  # 20
