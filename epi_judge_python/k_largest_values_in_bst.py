import itertools
from test_framework import generic_test, test_utils


def rev_order(tree):
    stack = []
    while stack or tree:
        if tree:
            stack.append(tree)
            tree = tree.right
        else:
            tree = stack.pop()
            yield tree.data
            tree = tree.left


def find_k_largest_in_bst(tree, k):
    return [x for x in itertools.islice(rev_order(tree), k)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
