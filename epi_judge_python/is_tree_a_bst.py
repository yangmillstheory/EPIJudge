from test_framework import generic_test


def _preorder(tree, key_min=float('-inf'), key_max=float('inf')):
    # T(n) = S(n) = O(n)
    if not tree:
        return True
    l, r, data = tree.left, tree.right, tree.data
    if data < key_min or data > key_max:
        return False
    return _preorder(l, key_min, min(key_max, data)) and _preorder(r, max(key_min, data), key_max)


def _inorder(tree):
    stack, prev = [], float('-inf')
    while stack or tree:
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            if tree.data < prev:
                return False
            prev = tree.data
            tree = tree.right
    return True


def is_binary_tree_bst(tree):
    return _inorder(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
