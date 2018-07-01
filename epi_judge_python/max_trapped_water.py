from test_framework import generic_test


def get_max_trapped_water(hs):
    # T(n) = O(n)
    lo, hi = 0, len(hs)-1
    _max_area = 0
    while lo <= hi:
        min_h, i = min([(hs[lo], lo), (hs[hi], hi)])
        _max_area = max(_max_area, (hi-lo)*min_h)
        if i == hi:
            hi -= 1
        else:
            lo += 1
    return _max_area


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_trapped_water.py",
                                       "max_trapped_water.tsv",
                                       get_max_trapped_water))
