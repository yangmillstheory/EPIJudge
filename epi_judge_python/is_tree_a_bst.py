from test_framework import generic_test


def is_binary_tree_bst(tree, key_min=float('-inf'), key_max=float('inf')):
    # T(n) = S(n) = O(n)
    if not tree:
        return True
    l, r, data = tree.left, tree.right, tree.data
    if data < key_min or data > key_max:
        return False
    return is_binary_tree_bst(l, key_min, min(key_max, data)) and is_binary_tree_bst(r, max(key_min, data), key_max)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
