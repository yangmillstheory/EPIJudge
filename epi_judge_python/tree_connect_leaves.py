import functools

from collections import deque
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class ListNode:
    def __init__(self, data, node):
        self.data = data
        self.next = node


def _iter_preorder(root):
    stack = deque()
    while root or stack:
        if root:
            if root.right:
                stack.append(root.right)
            yield root
            root = root.left
        else:
            root = stack.pop()


def _iter_leaves_preorder(root):
    for node in _iter_preorder(root):
        if not node.left and not node.right:
            yield node


def create_list_of_leaves(root):
    # represent a linked list node as a tuple
    res, node = [], ListNode(0, None)
    for leaf in _iter_leaves_preorder(root):
        node.next = ListNode(leaf.data, None)
        res.append(node.next)
        node = node.next
    return res


@enable_executor_hook
def create_list_of_leaves_wrapper(executor, tree):
    result = executor.run(functools.partial(create_list_of_leaves, tree))

    if any(x is None for x in result):
        raise TestFailure("Result list can't contain None")
    return [x.data for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_connect_leaves.py",
                                       "tree_connect_leaves.tsv",
                                       create_list_of_leaves_wrapper))
