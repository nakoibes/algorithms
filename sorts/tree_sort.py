from data_structures.binary_tree import BinarySearchTree, TreeNode


def traverse(node: TreeNode, result: list):
    if node == None:
        return
    traverse(node.left, result)
    result.append(node.value)
    traverse(node.right, result)


def tree_sort(array: list):
    tree = BinarySearchTree.create_from_list(array)
    result = list()
    traverse(tree.root, result)
    return result


if __name__ == '__main__':
    array = [5, 1, 45, 100, 4, 46, 78, 22, 11]
    print(tree_sort(array))
    # print(array)
