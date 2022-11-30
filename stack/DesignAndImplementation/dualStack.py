# Program to implement dual stack in a single array.
__test__ = True


class DualStack:
    def __init__(self, size: int):
        self.stack = []
        self.size = size

        # Top pointers for two stacks
        self.top1 = -1
        self.top2 = size

    def __str__(self):
        return str(self.stack)

    def push(self, whichStack: int, value: int) -> None:
        """
        Push the given `value` into the specified stack `whichStack`.

        Args:
            - whichStack (int) : Denotes the stack.
            - value (int) : The value to push into the stack.

        """
        if whichStack == 1:
            if not self.isFull():
                self.top1 += 1
                self.stack.append(value)
            else:
                print("The stack is Full.")
        else:
            if not self.isFull():
                self.top2 -= 1
                self.stack.insert(-1, value)
            else:
                print("The stack is Full.")

        print("The value inserted Successfully.")

    def pop(self, whichStack: int) -> int:
        """Return the top element from the specified stack and delete it."""
        if whichStack == 1:
            if not self.isEmpty(1):
                temp = self.top1
                self.top1 -= 1
                return self.stack.pop(temp)
            else:
                print("The stack is Empty.")
        else:
            if not self.isEmpty(2):
                self.top2 += 1
                temp = self.top1 + 1
                return self.stack.pop(temp)
            else:
                print("The stack is Empty.")

    def peek(self, whichStack: int) -> int:
        """Return the peek element of the specified stack."""
        if whichStack == 1:
            if not self.isEmpty(1):
                return self.stack[self.top1]
            else:
                print("The stack is Empty.")
        else:
            if not self.isEmpty(2):
                return self.stack[self.top1 + 1]
            else:
                print("The stack is Empty.")

    def isEmpty(self, whichStack: int) -> bool:
        """
        Return 'True' if the specified stack is empty.
        Args:
            - whichStack (int) : Denotes the stack. 1 for stack1 and 2 for stack2.

        Returns:
            - (bool) True if the stack is empty else False.
        """
        if whichStack == 1:
            if self.top1 == -1:
                return True
            else:
                return False
        else:
            if self.top2 == self.size:
                return True
            else:
                return False

    def isFull(self) -> bool:
        """Return 'True' if the stack is full."""
        if self.top1 == self.top2 - 1:
            return True
        else:
            return False




