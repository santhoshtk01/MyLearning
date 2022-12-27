# Program to implement circular queue with fixed size.


class CircularQueue:
    """
    Class to represent and give a structure to circular queue.

    Attributes:
        - queue (list) : Python's inbuilt data structure to implement queue.
        - size (int) : Size of the queue.
        - front (int) : The front index position of the queue.
        - rear (int) : The rear index position of the queue.
    """
    def __init__(self, size: int):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1
        print("Queue called..")

    def __str__(self):
        return str(self.queue)

    def __del__(self):
        pass

    def enQueue(self, value: int) -> None:
        """
        Enqueue the value into the front of the queue.
        Args:
            value: The value to add in the front of the queue.
        """
        if not self.isFull():
            if self.front == self.size - 1:
                self.front = 0
            else:
                self.front += 1
                if self.rear == -1:
                    self.rear = 0
            self.queue[self.front] = value
            print("The value inserted Successfully.")
        else:
            print("The queue is Full.")

    def deQueue(self) -> int:
        """Return the element in the `rear` position."""
        if not self.isEmpty():
            if self.rear == self.size - 1:
                self.rear = 0
            else:
                self.rear += 1

        # Initializing the dequeued position with `None`
        value = self.queue[self.rear - 1]
        self.queue[self.rear - 1] = None

        return value

    def peek(self) -> int:
        """Return the element in the `rear` position. That's the peek element."""
        return self.queue[self.rear]

    def isFull(self) -> bool:
        """Return 'True' if the queue is full. Otherwise, return 'False'."""
        if self.front + 1 == self.rear:
            return True
        if self.front == 0 and self.rear == self.size + 1:
            return True
        else:
            return False

    def isEmpty(self) -> bool:
        """Return 'True' if the queue is Empty. Otherwise, return 'False'."""
        if self.front + 1 == self.rear:
            return True
        else:
            return False

    def deleteCircularQueue(self) -> None:
        """Delete the entire circular queue."""
        self.queue = [None] * self.size




