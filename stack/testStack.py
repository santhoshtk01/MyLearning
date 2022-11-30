from dynamicStack import DynamicStack
from staticStack import StaticStack
from stackLL import Stack
from DesignAndImplementation import dualStack, specialStack
from random import randint

while True:
    speciStack = specialStack.SpecialStack(10)

    for _ in range(10):
        speciStack.push(randint(1, 10))

    speciStack.printStack()

    if speciStack.getMin() == min(speciStack.returnList()):
        print("Test case passed..")
        continue
    else:
        print("Test case failed.")
        break




# TODO : Test the special stack in various cases.
