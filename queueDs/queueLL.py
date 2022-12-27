# Program for Queue using linked list.


class Node:
    """
    Class to represent the Node.
    Attributes:
        - value (int) : The value of the Node object.
        - next (Node) : The reference of the next Node.
    """
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None


class LinkedList:
    """
    Class to create a singly linked list.
    Attributes:
        - head (Node) : The head of the linked list.
        - tail (Node) : The tail of the linked list.
    """
    def __init__(self):
        self.head = None
        self.tail = None


class Queue(LinkedList):
    """Class to represent the queue."""
    def __init__(self):
        # Calling the parent class initializer.
        super().__init__()

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp.value
            temp = temp.next

    def __str__(self):
        return str([value for value in self])

    def enQueue(self, value: int) -> None:
        """
        Enqueue the Node in the end of the linked list.
        Args:
            value: The value of the Node.
        """
        newNode = Node(value)

        # If the queue is Empty.
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        print("The value enqueued successfully.")

    def deQueue(self) -> Node:
        """Return the Node and dequeue the Node."""
        if not self.isEmpty():
            dequeuedNode = self.head
            self.head = self.head.next
            return dequeuedNode
        else:
            print("The queue is Empty.")

    def isEmpty(self) -> bool:
        """Return 'True' if the queue is Empty. Otherwise, return 'False'."""
        if self.head is None:
            return True
        else:
            return False

    def peek(self) -> Node:
        """Return the peek `Node` in the queue."""
        if not self.isEmpty():
            return self.head
        else:
            print("The queue is Empty.")

    def deleteQueue(self) -> None:
        """Delete the entire queue."""
        self.head = self.tail = None
        print("The Queue deleted successfully.")


