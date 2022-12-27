# Program to implement stack dynamically using Python's `list`.
__test__ = True


class DynamicStack:
    """
    Class to create a dynamic stack and perform operations on it.

    Attributes:
        - stack (list) : A Python's inbuilt list to represent as a stack.

    """
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack[::-1])

    def push(self, value: int) -> None:
        """
        Add the given element `value` to the end of the `stack`.
        Args:
            - value (int) : The value to be added to the stack.

        """
        self.stack.append(value)
        # print("Value {0} inserted successfully.".format(value))

    def pop(self) -> int:
        """Return the recently added element form the `stack` and delete it. """
        if self.isEmpty():
            print("The stack is Empty.")
        else:
            return self.stack.pop()

    def peek(self) -> int:
        """Return the peek element in the `stack`."""
        if self.isEmpty():
            print("The stack is Empty.")
        else:
            return self.stack[-1]

    def isEmpty(self) -> bool:
        """Return `False` value if the stack is empty."""
        if self.stack:
            return False
        else:
            return True

    def deleteDynamicStack(self) -> None:
        self.stack = None

