from typing import Optional


class Node:
    def __init__(self, value: Optional[int] = None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


tree = Node(10)
tree.left = Node(5)
tree.right = Node(6)

print(tree)
