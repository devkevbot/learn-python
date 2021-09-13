class Node:
    def __init__(self, value: int, next: object = None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other: object) -> bool:
        return self.value == other.value


class LinkedList:
    def __init__(self, head: Node = None) -> None:
        self.head = head

    def __str__(self) -> str:
        printout = []
        curr_node = self.head
        while curr_node is not None:
            printout.append(str(curr_node))
            curr_node = curr_node.next

        return "->".join(printout)

    def __len__(self) -> int:
        curr_node = self.head
        count = 0
        while curr_node is not None:
            count += 1
            curr_node = curr_node.next

        return count

    def __contains__(self, value: int) -> bool:
        """
        Returns true if the linked list has at least one node which contains value
        """
        curr_node = self.head

        while curr_node is not None:
            if curr_node.value == value:
                return True
            curr_node = curr_node.next

        return False

    def front(self) -> None:
        """
        Returns the value contained in the head node
        """
        return self.head.value if self.head is not None else None

    @classmethod
    def from_list(cls, values: list) -> None:
        linked_list = LinkedList()
        for value in values:
            linked_list.add(value)
        return linked_list

    def add(self, value: int) -> None:
        """
        Appends a node containing value to the end of the list
        """
        curr_node = self.head

        if curr_node is None:
            self.head = Node(value)
            return

        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = Node(value)

    def remove(self, value: int) -> None:
        """
        Removes all nodes which contain value
        """
        curr_node = self.head
        prev_node = None

        while curr_node is not None:
            if curr_node.value == value:
                if curr_node is self.head:
                    self.head = curr_node.next
                    continue

                if prev_node is None:
                    prev_node = curr_node
                else:
                    prev_node.next = curr_node.next

                curr_node = curr_node.next
            else:
                prev_node = curr_node
                curr_node = curr_node.next

    def frequency(self, value: int) -> int:
        """
        Returns the number of nodes which contain value
        """
        curr_node = self.head
        freq = 0
        while curr_node is not None:
            if curr_node.value == value:
                freq += 1
            curr_node = curr_node.next

        return freq

    def reverse(self) -> None:
        """
        Reverses the linked list in-place
        """

        prev_node = None
        curr_node = self.head
        next_node = None

        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        self.head = prev_node
