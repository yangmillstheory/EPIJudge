from test_framework import generic_test


def search_smallest(a):
    # T(n) = O(log n)
    # S(n) = O(1)
    lo, hi = 0, len(a)-1
    while lo <= hi:
        mid = lo + (hi-lo)//2
        if a[mid] > a[hi]:
            lo = mid+1
        elif mid == 0 or (mid-1 >= 0 and a[mid-1] > a[mid]):
            return mid
        else:
            hi = mid-1
    raise RuntimeError


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
