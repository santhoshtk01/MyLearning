# Program to implement a special stack with 'getMin()' method.
from stack.staticStack import StaticStack
from typing import Union


class SpecialStack(StaticStack):
    """Class to create a stack with special functionalities."""
    def __init__(self, size: int):
        self.stack = StaticStack(size)
        self.auxStack = StaticStack(size)
        print(type(self.auxStack))

    def printStack(self):
        print("Stack : {}\nAuxiliary Stack : {}".format(self.stack, self.auxStack))

    def push(self, value: int) -> None:
        if not self.stack.isFull() and not self.auxStack.isFull():
            if self.stack.stack:
                # If the topStack > element add the element to the auxStack as well.
                if self.stack.peek() > value:
                    self.stack.stack.append(value)
                    self.auxStack.stack.append(self.stack.peek())
                else:
                    self.stack.stack.append(value)
            else:
                # If the both stacks are empty.
                self.stack.stack.append(value)
                self.auxStack.stack.append(value)
        else:
            print("The stack is full.")

    def pop(self) -> Union[int, tuple]:
        if self.auxStack.peek() <= self.stack.peek():
            return self.stack.pop(), self.auxStack.pop()
        else:
            return self.stack.pop()

    def getMin(self) -> int:
        if not self.stack.isEmpty() and not self.auxStack.isEmpty():
            return self.auxStack.peek()
        else:
            print("The stack is Empty..")
