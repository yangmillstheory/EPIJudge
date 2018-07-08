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


def range_lookup_in_bst(tree, interval):
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


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("range_lookup_in_bst.py",
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
