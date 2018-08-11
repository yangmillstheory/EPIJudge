import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class Dummy:
    def __init__(self):
        self.right = None


def bst_to_doubly_linked_list_extra_memory(root):
    '''Convert a BST to a sorted doubly-linked list in O(n) time and space.'''
    prev = dummy = Dummy()
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            prev.right, node.left = node, prev
            prev, root = node, node.right
    root = dummy.right
    if root:
        root.left = None
    return root


def bst_to_doubly_linked_list(root):
    def _build_list(node):
        if node is None:
            return None, None
        prev_node, next_node = _build_list(node.left), _build_list(node.right)
        if prev_node[1]:
            prev_node[1].right, node.left = node, prev_node[1]
        if next_node[0]:
            next_node[0].left, node.right = node, next_node[0]
        return prev_node[0] or node, next_node[1] or node
    return _build_list(root)[0]


@enable_executor_hook
def bst_to_doubly_linked_list_wrapper(executor, tree):
    l = executor.run(functools.partial(bst_to_doubly_linked_list, tree))

    if l is not None and l.left is not None:
        raise TestFailure(
            'Function must return the head of the list. Left link must be None'
        )

    v = []
    while l:
        v.append(l.data)
        if l.right and l.right.left is not l:
            raise TestFailure('List is ill-formed')
        l = l.right

    return v


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_to_sorted_list.py",
                                       'bst_to_sorted_list.tsv',
                                       bst_to_doubly_linked_list_wrapper))
