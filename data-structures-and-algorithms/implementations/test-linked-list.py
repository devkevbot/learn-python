import unittest

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_len(self):
        linked_list = LinkedList()
        initial_values = [10, 15, 20, 30, 20]

        self.assertEqual(len(linked_list), 0)

        for value in initial_values:
            linked_list.add(value)

        self.assertEqual(len(linked_list), len(initial_values))

        linked_list.remove(20)

        self.assertEqual(len(linked_list), 3)

    def test_contains(self):
        linked_list = LinkedList()
        initial_values = [10, 15, 20, 30, 20]

        for value in initial_values:
            linked_list.add(value)

        self.assertTrue(10 in linked_list)
        self.assertTrue(15 in linked_list)
        self.assertTrue(20 in linked_list)
        self.assertTrue(30 in linked_list)
        self.assertFalse(-1 in linked_list)
        self.assertFalse(40 in linked_list)

    def test_front(self):
        linked_list = LinkedList()
        initial_values = [10, 15, 20, 30, 20]

        self.assertIsNone(linked_list.front())

        for value in initial_values:
            linked_list.add(value)

        self.assertEqual(linked_list.front(), 10)

        linked_list.remove(10)

        self.assertEqual(linked_list.front(), 15)

    def test_add(self):
        linked_list = LinkedList()
        initial_values = [10, 15, 20, 30, 20]

        for value in initial_values:
            linked_list.add(value)

        curr_node = linked_list.head
        node_idx = 0

        while curr_node is not None:
            desired = initial_values[node_idx]
            actual = curr_node.value

            self.assertEqual(desired, actual)
            node_idx += 1
            curr_node = curr_node.next

    def test_remove(self):
        linked_list = LinkedList()
        initial_values = [10, 15, 20, 30, 20]
        final_values = [10, 15, 30]

        for value in initial_values:
            linked_list.add(value)

        linked_list.remove(20)

        curr_node = linked_list.head
        node_idx = 0

        while curr_node is not None:
            desired = final_values[node_idx]
            actual = curr_node.value

            self.assertEqual(desired, actual)
            node_idx += 1
            curr_node = curr_node.next

    def test_frequency(self):
        linked_list = LinkedList()
        initial_values = [10, 15, 20, 30, 20]

        for value in initial_values:
            linked_list.add(value)

        self.assertEqual(linked_list.frequency(10), 1)
        self.assertEqual(linked_list.frequency(15), 1)
        self.assertEqual(linked_list.frequency(20), 2)
        self.assertEqual(linked_list.frequency(30), 1)
        self.assertEqual(linked_list.frequency(-1), 0)

    def test_reverse(self):
        linked_list = LinkedList()
        initial_values = [10, 15, 20, 30, 20]
        final_values = [20, 30, 20, 15, 10]

        for value in initial_values:
            linked_list.add(value)

        linked_list.reverse()

        curr_node = linked_list.head
        node_idx = 0

        while curr_node is not None:
            desired = final_values[node_idx]
            actual = curr_node.value

            self.assertEqual(desired, actual)
            node_idx += 1
            curr_node = curr_node.next


if __name__ == "__main__":
    unittest.main()
