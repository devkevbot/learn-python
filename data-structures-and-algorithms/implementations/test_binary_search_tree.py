import unittest

from binary_search_tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self) -> None:
        self.nodes_values = [10, 5, 15, 10, 20, 35, 3, 7, 2]
        self.bst = BinarySearchTree.from_list([10, 5, 15, 10, 20, 35, 3, 7, 2])

    def test_contains(self) -> None:
        for value in self.nodes_values:
            self.assertTrue(value in self.bst)

    def test_inorder_traversal(self) -> None:
        expected_order = [2, 3, 5, 7, 10, 10, 15, 20, 35]
        actual_order = []
        self.bst.inorder_traversal(actual_order)
        self.assertListEqual(expected_order, actual_order)

    def test_preorder_traversal(self) -> None:
        expected_order = [10, 5, 3, 2, 7, 15, 10, 20, 35]
        actual_order = []
        self.bst.preorder_traversal(actual_order)
        self.assertListEqual(expected_order, actual_order)

    def test_postorder_traversal(self) -> None:
        expected_order = [2, 3, 7, 5, 10, 35, 20, 15, 10]
        actual_order = []
        self.bst.postorder_traversal(actual_order)
        self.assertListEqual(expected_order, actual_order)

    def test_invert(self) -> None:
        expected_order = [35, 20, 15, 10, 10, 7, 5, 3, 2]
        actual_order = []
        self.bst.invert()
        self.bst.inorder_traversal(actual_order)
        self.assertListEqual(expected_order, actual_order)


if __name__ == "__main__":
    unittest.main()
