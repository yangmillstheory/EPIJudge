from test_framework import generic_test


def apply_permutation(p, a):
    for i in range(len(p)):
        j, prev = i, a[i]
        while p[j] is not None:
            a[p[j]], prev = prev, a[p[j]]
            temp = p[j]
            p[j] = None
            j = temp


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
