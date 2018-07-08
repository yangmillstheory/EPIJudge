import functools
from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def _min_height_bst(a, lo, hi):
    if lo > hi:
        return
    mid = lo + (hi-lo)//2
    tree = BstNode(a[mid])
    tree.left, tree.right = _min_height_bst(a, lo, mid-1), _min_height_bst(a, mid+1, hi)
    return tree


def _recursive(a):
    # T(n) = O(n)
    # S(n) = O(log n)
    return _min_height_bst(a, 0, len(a)-1)


def _iterative(a):
    root, stack = None, [(0, len(a)-1, None, None)]
    while stack:
        lo, hi, l_parent, r_parent = stack.pop()
        if lo > hi:
            continue
        mid = lo + (hi-lo)//2
        node = BstNode(a[mid])
        root = root or node
        if l_parent:
            l_parent.right = node
        if r_parent:
            r_parent.left = node
        stack.append((lo, mid-1, None, node))
        stack.append((mid+1, hi, node, None))
    return root


def build_min_height_bst_from_sorted_array(a):
    return _iterative(a)


@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure("Result binary tree mismatches input array")
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "bst_from_sorted_array.py", 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))
