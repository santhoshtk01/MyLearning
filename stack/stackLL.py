# Program to implement stack using linked list.


class Node:
    """Class to represent a node."""
    def __init__(self, value: int):
        self.value = value
        self.next = None


class LinkedList:
    """Class to represent a linked list."""
    def __init__(self):
        self.head = None


class Stack:
    """Class to represent the stack using linked list."""
    def __init__(self):
        self.stack = LinkedList()
        print("Created..")

    def __iter__(self):
        temp = self.stack.head
        while temp:
            yield temp
            temp = temp.next

    def __str__(self):
        values = ""
        for node in self:
            values += str(node.value)
            values += " -> "

        return values

    def push(self, value: int) -> None:
        """
        Create a new Node with the value and push the Node into the linked list.

        params:
        - value (int) : The value of the node.

        """
        newNode = Node(value)

        if self.stack.head is None:
            self.stack.head = newNode
        else:
            newNode.next = self.stack.head
            self.stack.head = newNode
        print("Value {0} pushed successfully.".format(value))

    def pop(self) -> Node:
        """Return the head Node and delete the head node."""
        if not self.isEmpty():
            temp = self.stack.head
            self.stack.head = temp.next
            return temp
        else:
            print("The stack is Empty.")

    def peek(self) -> Node:
        """Return the peek element of the linked list."""
        if not self.isEmpty():
            return self.stack.head
        else:
            print("The stack is Empty.")

    def isEmpty(self) -> bool:
        """Return `True` if the stack is Empty."""
        if self.stack.head is None:
            return True
        else:
            return False

    def delete(self):
        """Delete the entire stack."""
        if not self.isEmpty():
            for node in self:
                node.next = None

        self.stack.head = None
        print("Deleted successfully.")