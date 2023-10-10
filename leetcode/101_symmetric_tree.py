# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


from typing import Optional


def check_symmetric_equality(left_tree, right_tree):
    if left_tree is None or right_tree is None:
        if left_tree is None and right_tree is None:
            return True
        return False
    if left_tree.val != right_tree.val:
        return False
    if check_symmetric_equality(left_tree.left, right_tree.right) and check_symmetric_equality(left_tree.right,
                                                                                               right_tree.left):
        return True
    return False


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return check_symmetric_equality(root.left, root.right)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_nodes = list()
        right_nodes = list()
        next_nodes = deque()
        next_nodes.appendleft(root.left)
        while next_nodes:
            node = next_nodes.pop()
            if node:
                left_nodes.append(node)
                next_nodes.appendleft(node.left)
                next_nodes.appendleft(node.right)
            else:
                left_nodes.append(TreeNode(None))

        next_nodes.appendleft(root.right)
        while next_nodes:
            node = next_nodes.pop()
            if node:
                right_nodes.append(node)
                next_nodes.appendleft(node.right)
                next_nodes.appendleft(node.left)
            else:
                right_nodes.append(TreeNode(None))

        for left_node, right_node in zip(left_nodes, right_nodes):
            if left_node.val != right_node.val:
                return False

        return True


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_nodes = [root.left]
        right_nodes = [root.right]
        while left_nodes and right_nodes:
            left = left_nodes.pop()
            right = right_nodes.pop()

            if left is None or right is None:
                if left is None and right is None:
                    continue
                else:
                    return False
            elif left.val != right.val:
                return False

            left_nodes.append(left.right)
            left_nodes.append(left.left)
            right_nodes.append(right.left)
            right_nodes.append(right.right)

        return True

        # if left.right is None:
        #     left_nodes.append(TreeNode(None))
        # else:
        #     left_nodes.append(left.right)
        # if left.left is None:
        #     left_nodes.append(TreeNode(None))
        # else:
        #     left_nodes.append(left.left)
        #
        # if right.left is None:
        #     right_nodes.append(TreeNode(None))
        # else:
        #     right_nodes.append(left.right)
        # if right.right is None:
        #     right_nodes.append(TreeNode(None))
        # else:
        #     right_nodes.append(left.left)

        # return True
        # right_nodes.append(right.left)
        # right_nodes.append(right.right)

        # next_nodes = deque()
        # next_nodes.appendleft(root.left)
        # while next_nodes:
        #     node = next_nodes.pop()
        #     if node:
        #         left_nodes.append(node)
        #         next_nodes.appendleft(node.left)
        #         next_nodes.appendleft(node.right)
        #     else:
        #         left_nodes.append(TreeNode(None))
        #
        # next_nodes.appendleft(root.right)
        # while next_nodes:
        #     node = next_nodes.pop()
        #     if node:
        #         right_nodes.append(node)
        #         next_nodes.appendleft(node.right)
        #         next_nodes.appendleft(node.left)
        #     else:
        #         right_nodes.append(TreeNode(None))
        #
        # for left_node, right_node in zip(left_nodes, right_nodes):
        #     if left_node.val != right_node.val:
        #         return False
        #
        # return True


if __name__ == '__main__':
    s = Solution()

    node0 = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(1)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node5 = TreeNode(3)
    node6 = TreeNode(2)
    node0.left = node1
    node0.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6

    # node0 = TreeNode(1)
    # node1 = TreeNode(2)
    # node2 = TreeNode(2)
    # node3 = TreeNode(3)
    # node4 = TreeNode(3)
    # node0.left = node1
    # node0.right = node2
    # # node1.left = node3
    # node1.right = node3
    # # node2.left = node5
    # node2.right = node4

    print(s.isSymmetric(node0))
