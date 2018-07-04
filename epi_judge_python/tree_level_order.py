from collections import deque, namedtuple
from test_framework import generic_test


NodeWithDepth = namedtuple('NodeWithDepth', ['node', 'depth'])


def binary_tree_depth_order(root):
    # T(n) = S(n) = O(n)
    levels = []
    if not root:
        return levels
    q = deque([NodeWithDepth(root, 0)])
    while q:
        node, depth = q.popleft()
        if len(levels) == depth:
            levels.append([])
        levels[depth].append(node.data)
        if node.left:
            q.append(NodeWithDepth(node.left, depth+1))
        if node.right:
            q.append(NodeWithDepth(node.right, depth+1))
    return levels


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
