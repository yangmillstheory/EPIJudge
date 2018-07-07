from test_framework import generic_test


def find_first_greater_than_k(tree, k):
    '''Return a strict ceiling node for an integer k
    in logarithmic time.
    '''
    cand = None
    while tree:
        if tree.data > k:
            cand = tree
            tree = tree.left
        else:
            tree = tree.right
    return cand


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
