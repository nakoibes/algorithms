# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_BST(root, max_val, min_val):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return root.val < max_val and root.val > min_val
    else:
        return (root.val < max_val and root.val > min_val and check_BST(root.right, max_val, max(min_val, root.val))
                and check_BST(root.left, min(max_val, root.val), min_val))


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return check_BST(root, float("inf"), -float("inf"))
