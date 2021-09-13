class BinarySearchTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __contains__(self, value: int) -> bool:
        """
        Return True if the binary search tree contains at least one node containing value
        """
        if value < self.value:
            if self.left is None:
                return False

            return self.left.__contains__(value)
        elif value > self.value:
            if self.right is None:
                return False

            return self.right.__contains__(value)
        else:
            return True

    @classmethod
    def from_list(cls, values: list) -> object:
        bst = cls(values[0])
        for value in values[1:]:
            bst.insert(value)
        return bst

    def insert(self, value: int) -> None:
        """
        Inserts value following the binary search tree invariant as follows:
        - All values to the left of a given node are strictly less than the node value.
        - All values to the right of a given node are greater than or equal to the node value.
        """

        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def remove(self, value: int) -> None:
        pass

    def inorder_traversal(self, visited: list) -> None:
        if self.left is not None:
            self.left.inorder_traversal(visited)

        visited.append(self.value)

        if self.right is not None:
            self.right.inorder_traversal(visited)

    def preorder_traversal(self, visited: list) -> None:
        visited.append(self.value)

        if self.left is not None:
            self.left.preorder_traversal(visited)

        if self.right is not None:
            self.right.preorder_traversal(visited)

    def postorder_traversal(self, visited: list):
        if self.left is not None:
            self.left.postorder_traversal(visited)

        if self.right is not None:
            self.right.postorder_traversal(visited)

        visited.append(self.value)

    def invert(self):
        """
        Inverts the binary tree in-place.
        """
        self.left, self.right = self.right, self.left

        if self.left is not None:
            self.left.invert()

        if self.right is not None:
            self.right.invert()
