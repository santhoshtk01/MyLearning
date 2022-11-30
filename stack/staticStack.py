# Program for static implementation of stack using Python's list.
__test__ = True


class StaticStack:
    """
    Class for static stack using Python's `list`.

    Attributes:
        - stack (list) : Python's inbuilt data structure for stack.
        - size (int) : The maximum elements can be stored in the stack.

    """
    def __init__(self, size: int):
        """Creates a new static stack."""
        self.stack = []
        self.size = size

    def __str__(self):
        return str(self.stack[::-1])

    def returnList(self):
        return self.stack[::-1]

    def push(self, value: int) -> None:
        """
        Push the given value into the stack.

        Args:
            - value (int): The value to be added at the end of the stack.

        """
        if self.isFull():
            print("The stack is Full.")
        else:
            self.stack.append(value)
            print("Value {0} inserted successfully.".format(value))

    def pop(self) -> int:
        """Return the recently added value and delete it."""
        if self.isEmpty():
            print("The stack is Empty.")
        else:
            return self.stack.pop()

    def peek(self) -> int:
        """Return the recently added element."""
        if self.isEmpty():
            print("The stack is Empty.")
        else:
            return self.stack[-1]

    def isEmpty(self) -> bool:
        """Return `True` if the stack is empty."""
        if not self.stack:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """Return `True` if the stack is full."""
        if len(self.stack) == self.size:
            return True
        else:
            return False


