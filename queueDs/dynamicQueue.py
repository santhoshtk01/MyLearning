# Program to implement queue using Python's list dynamically.
__test__ = True


class DynamicQueue:
    """
    Class to create a dynamic queue using Python's list.

    Attributes:
        - queue (list) : Python's inbuilt data structure to implement queue.

    More Details :
        Front -> [] <- Rear
    """
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def enQueue(self, value: int) -> None:
        """
        Enqueue the `value` into the Queue's rear.

        Args:
            - value (int) : The value to enqueue (insert) into the queue.
        """
        self.queue.append(value)
        # print("Value {0} enqueued successfully.".format(value))

    def deQueue(self) -> int:
        """Return the peek element from the queue and delete it. The front element."""
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            print("The queue is Empty.")

    def isEmpty(self) -> bool:
        """Return 'True' if the queue is Empty."""
        if not self.queue:
            return True
        else:
            return False

    def peek(self):
        """Return the peek element in the queue."""
        return self.queue[0]

    def deleteDynamicQueue(self) -> None:
        """Delete the entire queue."""
        if not self.isEmpty():
            self.queue = []
            print("Queue deleted successfully.")
        else:
            print("Queue is Empty.")
