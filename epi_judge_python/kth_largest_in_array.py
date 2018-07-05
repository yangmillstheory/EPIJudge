from test_framework import generic_test


def partition(a, lo, hi):
    mid = lo + (hi-lo)//2
    a[mid], a[hi] = a[hi], a[mid]
    j = lo  # points to first el. >= a[hi]
    for i in range(lo, hi):
        if a[i] < a[hi]:
            a[i], a[j] = a[j], a[i]
            j += 1
    a[j], a[hi] = a[hi], a[j]
    return j


def find_kth_largest(k, a):
    # T(n) = O(n)
    # S(n) = O(1)
    n = len(a)
    lo, hi = 0, n-1
    while lo <= hi:
        p = partition(a, lo, hi)
        if p == n-k:
            return a[p]
        elif p < n-k:
            lo = p+1
        else:
            hi = p-1
    raise RuntimeError


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
