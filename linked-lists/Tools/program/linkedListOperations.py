from generator import LinkedList, Node


class LinkedListOperations(LinkedList):
    """Class to perform various operations on the linked list."""

    def removeDuplicates(self):
        """
        Remove the duplicate nodes from the linked list. Ready to use method.

        ================================================================
        NOTE : This method has tested in various cases and ready to use.
        ================================================================
        """
        duplicates = self.findDuplicates()
        currentNode = self.head
        previousNode = self.head
        flag = True

        while currentNode.next:
            if currentNode.value in duplicates:
                if currentNode == self.head:
                    self.head = currentNode.next
                elif currentNode.next is None:
                    previousNode.next = None
                else:
                    flag = False
                    previousNode.next = currentNode.next
            if flag:
                previousNode = currentNode
            currentNode = currentNode.next

    def findDuplicates(self) -> list:
        """Return duplicate elements in the linked list as list."""
        visited = []
        duplicates = set()

        for node in self:
            if node in visited:
                duplicates.add(node)
            visited.append(node)

        return list(duplicates)

    def returnNodeFromLast(self, n: int) -> int:
        """
        Return the nth node value from the linked list starting from last.
        Args:
            n: The nth node to be found in the linked list form the last.

        Returns: The value of the nth node.

        ================================================================
        NOTE : This method has tested in various cases and ready to use.
        ================================================================
        """
        pointerOne = self.head
        pointerTwo = self.head

        # To set the pointerTwo
        location = 1
        while location <= n and pointerTwo.next:
            location += 1
            pointerTwo = pointerTwo.next
        else:
            print("Index out of range..")
            exit(0)

        # Finding the nth node form the last in the linked list.
        while pointerTwo:
            pointerOne = pointerOne.next
            pointerTwo = pointerTwo.next

        return pointerOne.value

    def partition(self, value: int) -> None:
        """
        Partition the linked list based on the given value (int).

        More Details :
        - The node value less than and equal to the `value` are on the left side.
        - The node value greater than the `value` are on the right side of the linked list.

        Example:
            - Input : 11 -> 3 -> 9 -> 10 -> 15
            - Output : 3 -> 9 -> 11 -> 10 -> 15

        Args:
            - value (int) : The value to be compared with each node value in the linked list.

        ================================================================
        NOTE : This method has tested in various cases and ready to use.
        ================================================================
        """
        leftHead = leftList = None
        rightHead = rightList = None

        trackNode = self.head

        while trackNode:
            if trackNode.value >= value:
                # Add the node to the right list.
                if rightHead is None:
                    rightHead = trackNode
                    rightList = rightHead
                else:
                    rightList.next = trackNode
                    rightList = rightList.next
            else:
                # Add the node to the left list.
                if leftHead is None:
                    leftHead = trackNode
                    leftList = leftHead
                else:
                    leftList.next = trackNode
                    leftList = leftList.next

            trackNode = trackNode.next

        # Combining the nodes.
        rightList.next = None
        leftList.next = rightHead
        self.head = leftHead

    @staticmethod
    def reverseLinkedList(linkedList: LinkedList):
        """Reverse the given linked list."""
        previousNode = None
        currentNode = linkedList.head
        nextNode = linkedList.head

        while currentNode:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode

        # Updating the head of the linked list.
        linkedList.head = previousNode

        return linkedList

    @staticmethod
    def returnSum(linkedList: LinkedList) -> int:
        """
        Return the sum of the given linked list.
        Args:
            - linkedList (LinkedList) : The linked list to be summed up.

        Returns:
            - (int) The sum of the node values in the linked list.
        """
        total = 0
        temp = linkedList.head

        while temp:
            total = total * 10 + temp.value
            temp = temp.next

        return total

    def sumLinkedList(self, linkedListOne: LinkedList, linkedListTwo: LinkedList):
        """
        Return the sum of the linked list.

        Args:
            - linkedList (LinkedList) : The linked list to be added with the self linked list.

        More Details:
        Given a head of two linked list, so you have to sum up them and return them as a
        linked list. The linked list will be given in reverse order.

        Example :
        - Input : 1 -> 2 -> 4 and 5 -> 7 -> 9
        - Output : 6 -> 9 -> 3 -> 1

        Explanation:
        421 + 975 = 1396

        """
        listOneSum = 0
        listTwoSum = 0

        # Reversing the list
        l1 = self.reverseLinkedList(linkedListOne)
        l2 = self.reverseLinkedList(linkedListTwo)

        listOneSum += self.returnSum(l1)
        listTwoSum += self.returnSum(l2)

        total = listOneSum + listTwoSum

        # Creating a new linked list with the sum value.
        newLinkedList = LinkedList(0)
        newLinkedList.head = Node(int(str(total)[0]))
        temp = newLinkedList.head

        for value in str(total)[1:]:
            temp.next = Node(int(value))
            temp = temp.next

        return newLinkedList

    @staticmethod
    def findIntersection(linkedList1: LinkedList, linkedList2: LinkedList) -> Node:
        """
        Return the node that intersecting on the linked list.

        Args:
            - linkedList1 (LinkedList) : The first linked list.
            - linkedList2 (LinkedList) : The second linked list.

        Returns:
            - (Node) The intersecting node in the linked lists.
        """
        whichLL = None
        toSkip = None

        # Calculate how many nodes to skip in which linked list.
        if linkedList1.length > linkedList2.length:
            whichLL = "2"
            toSkip = linkedList1.length - linkedList2.length
        else:
            whichLL = "1"
            toSkip = linkedList2.length - linkedList1.length

        # Traversing through the linked list and skip the nodes in any one of them.
        head1 = linkedList1.head
        head2 = linkedList2.head

        while head1 != head2:
            # Updating the nodes
            if whichLL == "1" and toSkip:
                toSkip -= 1
            else:
                head1 = head1.next

            if whichLL == "2" and toSkip:
                toSkip -= 1
            else:
                head2 = head2.next

            return head1

