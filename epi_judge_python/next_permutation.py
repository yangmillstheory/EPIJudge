from test_framework import generic_test


def reverse(a, lo, hi):
    while lo < hi:
        a[lo], a[hi] = a[hi], a[lo]
        lo += 1
        hi -= 1


def next_permutation(a):
    n = len(a)
    for j in range(n-1, 0, -1):
        if a[j] > a[j-1]:
            k = j
            break
    else:
        return []
    for j in range(n-1, k-1, -1):
        if a[j] > a[k-1]:
            i = j
            break
    else:
        raise ValueError(a)
    a[i], a[k-1] = a[k-1], a[i]
    reverse(a, k, n-1)
    return a


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", 'next_permutation.tsv', next_permutation))
