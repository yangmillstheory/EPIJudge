import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def find_successor(root):
    '''In-order successor in a binary tree in O(h) time and O(1) space.'''
    if root.right:
        root = root.right
        while root.left:
            root = root.left
        return root
    elif root.parent:
        # this condition isn't really necessary given loop below, but it's clearer this way
        if root.parent.left == root:
            return root.parent
        while root.parent and root.parent.right == root:
            root = root.parent
        return root.parent


@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("successor_in_tree.py",
                                       'successor_in_tree.tsv',
                                       find_successor_wrapper))
