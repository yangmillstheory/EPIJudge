import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size


def find_kth_node_binary_tree(root, k):
    return kth_in_order_recursive(root, k)


def kth_in_order_recursive(root, k):
    if not root:
        return
    l, r = root.left, root.right
    if l:
        if k == l.size+1:
            return root
        if k < l.size+1:
            return kth_in_order_recursive(l, k)
        return kth_in_order_recursive(r, k-(l.size+1))
    if k == 1:
        return root
    return kth_in_order_recursive(r, k-1)


def kth_in_order_iterative(root, k):
    '''kth node in a binary tree with T(n) = O(h) and S(n) = O(1).'''
    while root:
        l_size = root.left.size if root.left else 0
        if l_size+1 == k:
            return root.data
        elif k <= l_size:
            root = root.left
        else:
            root = root.right
            k -= l_size+1


@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(
        functools.partial(find_kth_node_binary_tree, tree, k))

    if not result:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_node_in_tree.py",
                                       "kth_node_in_tree.tsv",
                                       find_kth_node_binary_tree_wrapper))
