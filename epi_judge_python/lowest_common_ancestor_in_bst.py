import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# Input nodes are nonempty and the key at s is less than or equal to that at b.
def _find_lca_recursive(tree, x, y):
    # T(n) = S(n) = O(h)
    if not tree:
        return
    if max(x.data, y.data) < tree.data:
        return _find_lca_recursive(tree.left, x, y)
    if min(x.data, y.data) > tree.data:
        return _find_lca_recursive(tree.right, x, y)
    return tree


def find_LCA(tree, x, y):
    while tree:
        data, l, r = tree.left, tree.right, tree.data
        if max(x.data, y.data) < data:
            tree = l
        if min(x.data, y.data) > data:
            tree = r
        else:
            break
    return tree


@enable_executor_hook
def lca_wrapper(executor, tree, s, b):
    result = executor.run(
        functools.partial(_find_lca_recursive, tree, must_find_node(tree, s),
                          must_find_node(tree, b)))
    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_in_bst.py",
                                       'lowest_common_ancestor_in_bst.tsv',
                                       lca_wrapper))
