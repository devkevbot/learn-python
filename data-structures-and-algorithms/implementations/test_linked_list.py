import unittest

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.initial_values = [10, 15, 20, 30, 20]
        self.linked_list = LinkedList.from_list([10, 15, 20, 30, 20])

    def test_len(self):
        self.assertEqual(len(self.linked_list), len(self.initial_values))
        self.linked_list.remove(20)
        self.assertEqual(len(self.linked_list), 3)

    def test_contains(self):
        self.assertTrue(10 in self.linked_list)
        self.assertTrue(15 in self.linked_list)
        self.assertTrue(20 in self.linked_list)
        self.assertTrue(30 in self.linked_list)
        self.assertFalse(-1 in self.linked_list)
        self.assertFalse(40 in self.linked_list)

    def test_front(self):
        self.assertIsNone(LinkedList().front())
        self.assertEqual(self.linked_list.front(), self.initial_values[0])
        self.linked_list.remove(self.initial_values[0])
        self.assertEqual(self.linked_list.front(), self.initial_values[1])

    def test_from_list(self):
        initial_values = [10, 15, 20, 30, 20]
        linked_list = LinkedList.from_list(initial_values)

        curr_node = linked_list.head
        node_idx = 0

        while curr_node is not None:
            desired = initial_values[node_idx]
            actual = curr_node.value

            self.assertEqual(desired, actual)
            node_idx += 1
            curr_node = curr_node.next

    def test_remove(self):
        final_values = [10, 15, 30]
        self.linked_list.remove(20)

        curr_node = self.linked_list.head
        node_idx = 0

        while curr_node is not None:
            desired = final_values[node_idx]
            actual = curr_node.value

            self.assertEqual(desired, actual)
            node_idx += 1
            curr_node = curr_node.next

    def test_frequency(self):
        self.assertEqual(self.linked_list.frequency(10), 1)
        self.assertEqual(self.linked_list.frequency(15), 1)
        self.assertEqual(self.linked_list.frequency(20), 2)
        self.assertEqual(self.linked_list.frequency(30), 1)
        self.assertEqual(self.linked_list.frequency(-1), 0)

    def test_reverse(self):
        final_values = [20, 30, 20, 15, 10]
        self.linked_list.reverse()

        curr_node = self.linked_list.head
        node_idx = 0

        while curr_node is not None:
            desired = final_values[node_idx]
            actual = curr_node.value

            self.assertEqual(desired, actual)
            node_idx += 1
            curr_node = curr_node.next


if __name__ == "__main__":
    unittest.main()
