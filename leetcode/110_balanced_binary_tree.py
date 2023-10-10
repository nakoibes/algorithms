# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def compare_max_depth(node):
            if node is None:
                return True, 0
            left_subtree = compare_max_depth(node.left)
            right_subtree = compare_max_depth(node.right)
            if not left_subtree[0] or not right_subtree[0]:
                return False, 0
            elif abs(left_subtree[1] - right_subtree[1]) > 1:
                return False, 0

            return True, max(left_subtree[1] + 1, right_subtree[1] + 1)

        return compare_max_depth(root)[0]



