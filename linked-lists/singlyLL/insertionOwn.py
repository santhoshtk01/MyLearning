# Program to insert a new node in the Linked List. Can be done in 3 ways
# 1. Inserting at the beginning
# 2. Inserting at the end
# 3. Inserting after a particular Node

# Creating a linked list
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertNode(self, value, location: str):
        """
        To insert a node in the linked list.
        Args:
            value: The value of the node.
            location: In which location do you want to add the node (last, first).

        TODO : This is my own implementation. Refer the instructor implementation
         to know insertion in between a node.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        elif location == 'first':
            # Adding node at the beginning
            new_node.next = self.head
            self.head = new_node
        elif location == 'last':
            new_node.next = self.tail
            self.tail = new_node


ll = LinkedList()
ll.InsertNode(10, 'last')
ll.InsertNode(20, 'first')
ll.InsertNode(100, 'last')

print(ll.head.value) # 20
print(ll.head.next.value) # 10
print(ll.tail.next.value) # 100
