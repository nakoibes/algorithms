# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums) - 1

        def create_tree(left, right):

            if left == right:
                return TreeNode(nums[left])
            elif right < left:
                return
            middle = (left + right) // 2
            node = TreeNode(nums[middle])
            node.left = create_tree(left, middle - 1)
            node.right = create_tree(middle + 1, right)
            return node

        return create_tree(0, len(nums) - 1)
