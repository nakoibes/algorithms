from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self, value):
        #kostil
        if isinstance(value, TreeNode):
            self.root = value
        else:
            self.root = TreeNode(value)

    def _print_tree_depth(self, node: TreeNode):
        print(node.value)
        if node.left is not None:
            self._print_tree_depth(node.left)
        if node.right is not None:
            self._print_tree_depth(node.right)

    def print_tree_depth(self):
        self._print_tree_depth(self.root)

    def find_max_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.find_max_depth(root.left), self.find_max_depth(root.right)) + 1

    def print_tree(self):
        max_depth = self.find_max_depth(self.root)
        width = (2 ** max_depth) - 1

        def form_str(node: TreeNode, start: int, finish: int) -> list[str]:
            if node is None:
                return [" "] * (finish - start + 1)
            middle = (start + finish) // 2
            return [" "] * middle + [str(node.value)] + [" "] * middle

        nodes = deque()
        nodes.appendleft(self.root)
        # left = 0
        # right = width - 1
        # window_width = right - left
        for i in range(max_depth):
            current_string = list()
            current_window = (2 ** (max_depth - i)) - 1
            for j in range(2 ** i):
                current_node = nodes.pop()
                current_string.extend(form_str(current_node, j*current_window+1, (current_window * (j + 1)) - 1))
                nodes.appendleft(current_node.left)
                nodes.appendleft(current_node.right)

            print("".join(current_string))

    # def _print_tree_width(self, node: TreeNode):
    #     print(node.value)
    #     if node.left is not None:
    #         self._print_tree_width(node.left)
    #     if node.right is not None:
    #         self._print_tree_width(node.right)
    #
    # def print_tree_width(self):
    #     self._print_tree_width(self.root)


class BinarySearchTree(BinaryTree):
    def __init__(self, value):
        super(BinarySearchTree, self).__init__(value)

    def _insert(self, node: TreeNode, value):
        if value <= node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def insert(self, value):
        self._insert(self.root, value)

    def insert_iter(self, value):
        node = self.root

        while node:
            last_node = node
            if node.value < value:
                node = node.right
            else:
                node = node.left

        if last_node.value < value:
            last_node.right = TreeNode(value)
        else:
            last_node.left = TreeNode(value)

    @classmethod
    def create_from_list(cls, value_list: list):
        tree = cls(value_list[0])
        for i in range(1, len(value_list)):
            tree.insert(value_list[i])
        return tree


def traverse_tree(node: TreeNode):
    next_nodes = deque()
    print(node.value)
    next_nodes.appendleft(node.left)
    next_nodes.appendleft(node.right)
    while next_nodes:
        node = next_nodes.pop()
        if node:
            print(node.value)
            next_nodes.appendleft(node.left)
            next_nodes.appendleft(node.right)


def rotate_tree(root: TreeNode):
    if root is None:
        return
    rotate_tree(root.left)
    rotate_tree(root.right)
    root.left, root.right = root.right, root.left


if __name__ == '__main__':
    # array = [8, 20, 6, 1, 43]
    # tree = BinarySearchTree.create_from_list(array)
    # tree.print_tree_depth()

    # tree = BinarySearchTree(10)
    # tree.insert(1)
    # tree.insert(20)
    # tree.insert(6)
    # tree.insert(8)
    # tree.insert(43)
    # tree.print_tree()

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node3.left = node5
    node3.right = node6
    node2.left = node4
    node1.left = node2
    node1.right = node3
    node2.right = node7

    tree = BinaryTree(node1)
    tree.print_tree()
    # traverse_tree(node1)
    # print("--")
    rotate_tree(node1)
    tree.print_tree()
    # print("--")
    # traverse_tree(node1)
