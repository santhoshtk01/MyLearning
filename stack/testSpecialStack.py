import unittest
from stack.DesignAndImplementation import specialStack
from random import randint


class MyTestCase(unittest.TestCase):
    def test_something(self):
        speciStack = specialStack.SpecialStack(10)
        for _ in range(10):
            speciStack.push(randint(1, 10))
        self.assertEqual(speciStack.getMin(), min(speciStack.returnList()))  # add assertion here


if __name__ == '__main__':
    unittest.main()
