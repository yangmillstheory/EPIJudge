import collections

from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def floor(tree, key):
    cand = None
    while tree:
        if tree.data <= key:
            cand, tree = tree, tree.right
        else:
            tree = tree.left
    return cand


def ceiling(tree, key):
    cand = None
    while tree:
        if tree.data >= key:
            cand, tree = tree, tree.left
        else:
            tree = tree.right
    return cand


def successor(tree, node):
    cand = None
    while tree:
        if tree.data > node.data:
            cand, tree = tree, tree.left
        else:
            tree = tree.right
    return cand


def _range_lookup_wo_stack(tree, interval):
    '''Find the range of keys in a BST within a closed interval in O(L*h) time.'''
    res = []
    if not tree:
        return res
    a, b = interval
    x, y = ceiling(tree, a), floor(tree, b)
    if not x or not y:
        return res
    while x and a <= x.data <= b:
        res.append(x.data)
        if x == y:
            break
        x = successor(tree, x)
    return res


def _range_lookup_recursive(tree, interval, res=None):
    if res is None:
        res = []
    if not tree:
        return res
    a, b = interval
    if a <= tree.data <= b:
        _range_lookup_recursive(tree.left, interval, res)
        res.append(tree.data)
        _range_lookup_recursive(tree.right, interval, res)
    elif a <= tree.data:
        _range_lookup_recursive(tree.left, interval, res)
    elif tree.data <= b:
        _range_lookup_recursive(tree.right, interval, res)
    return res


def _range_lookup_w_stack(tree, interval):
    a, b = interval
    res, stack = [], []
    while stack or tree:
        if tree:
            if a <= tree.data <= b:
                stack.append(tree)
                tree = tree.left
            elif a <= tree.data:
                tree = tree.left
            elif tree.data <= b:
                tree = tree.right
            else:
                tree = None
        else:
            tree = stack.pop()
            if tree.data <= b:
                res.append(tree.data)
                tree = tree.right
            else:
                tree = None
    return res


def range_lookup_in_bst(tree, interval):
    return _range_lookup_w_stack(tree, interval)
    # return _range_lookup_recursive(tree, interval)
    # return _range_lookup_wo_stack(tree, interval)


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("range_lookup_in_bst.py",
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
