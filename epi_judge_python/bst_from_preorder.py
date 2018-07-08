import collections
from bst_node import BstNode
from test_framework import generic_test


def _reconstruct(q, data_min=float('-inf'), data_max=float('inf')):
    if not q:
        return
    data = q[0]
    if data < data_min or data > data_max:
        return
    q.popleft()
    return BstNode(
        data,
        _reconstruct(q, data_min, min(data_max, data)),
        _reconstruct(q, max(data_min, data), data_max)
    )


def rebuild_bst_from_preorder(seq):
    # T(n) = S(n) = O(n)
    return _reconstruct(collections.deque(seq))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
