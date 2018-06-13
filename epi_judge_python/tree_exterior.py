import functools
import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def l_side(root, res):
    if not root:
        return
    if _is_leaf(root):
        return
    res.append(root)
    if root.left:
        l_side(root.left, res)
    else:
        l_side(root.right, res)


def leaves(root, orig, res):
    if not root:
        return
    if _is_leaf(root) and root is not orig:
        res.append(root)
    leaves(root.left, orig, res)
    leaves(root.right, orig, res)


def r_side(root, res):
    if not root or _is_leaf(root):
        return
    if root.right:
        r_side(root.right, res)
    else:
        r_side(root.left, res)
    res.append(root)


def _is_leaf(root):
    return not root.right and not root.left


def exterior_binary_tree(root):
    if not root:
        return []
    res = [root]
    if _is_leaf(root):
        return res
    l_side(root.left, res)
    leaves(root, root, res)
    r_side(root.right, res)
    return res


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_exterior.py", 'tree_exterior.tsv',
                                       create_output_list_wrapper))
