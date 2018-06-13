from test_framework import generic_test


def inorder_traversal(root):
    return list(it(root))


def it(root):
    '''In-order traversal in a tree with parent pointers.

    T(n) = O(n)
    S(n) = O(1)
    '''
    prev = None
    while root:
        if prev is root.parent:
            while root.left:
                root = root.left
            yield root.data
            prev, root = root, root.right or root.parent
        elif prev is root.left:
            yield root.data
            prev, root = root, root.right or root.parent
        else:
            prev, root = root, root.parent


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
