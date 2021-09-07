# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSumsHelper(root, branch_sum, list_of_sums):
    """
    Recursive solution
    Time: O(n) because we have to traverse through all n nodes.
    Space: O(n) because...
        Recursion:
            Average case: log(n) frames on the call stack from recursion
            Worst case: n frame on the call stack from recursion
        Branch sums:
            Number of branches in a binary tree which is dictated by
            the number of leaf nodes in a binary tree (math heavy).
            Worse case: n branch sums
    """
    if root is None:
        return

    new_sum = branch_sum + root.value

    if root.left is None and root.right is None:
        list_of_sums.append(new_sum)
    else:
        branchSumsHelper(root.left, new_sum, list_of_sums)
        branchSumsHelper(root.right, new_sum, list_of_sums)


def branchSums(root):
    # Write your code here.
    list_of_sums = []
    branchSumsHelper(root, 0, list_of_sums)
    return list_of_sums
