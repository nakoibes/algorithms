# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """Too slow"""
        if root is None:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left_depth == 0 or right_depth == 0:
            if left_depth == 0 and right_depth == 0:
                return 1
            else:
                return max(left_depth, right_depth) + 1
        return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)


from collections import deque


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        nodes = deque()
        nodes.appendleft((root, 1))
        while nodes:
            element = nodes.pop()
            node = element[0]
            left_node = node.left
            right_node = node.right
            if left_node is None and right_node is None:
                return element[1]
            if left_node is not None:
                nodes.appendleft((left_node, element[1] + 1))
            if right_node is not None:
                nodes.appendleft((right_node, element[1] + 1))
