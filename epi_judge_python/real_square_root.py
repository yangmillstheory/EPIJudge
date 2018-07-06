import math
from test_framework import generic_test


def square_root(x):
    lo, hi = float(0), max(x, 1)
    while not math.isclose(lo, hi):
        mid = lo + (hi-lo)/2
        if mid*mid > x:
            hi = mid
        else:
            lo = mid
    return lo


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("real_square_root.py",
                                       'real_square_root.tsv', square_root))
