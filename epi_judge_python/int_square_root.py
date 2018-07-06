from test_framework import generic_test


def _linear_time_sq_root(k):
    cand = 0
    for i in range(k+1):
        if pow(i, 2) <= k:
            cand = i
        else:
            break
    return cand


def _log_time_sq_root(k):
    lo, hi = 0, k
    cand = 0
    while lo <= hi:
        mid = lo + (hi-lo)//2
        if pow(mid, 2) <= k:
            cand, lo = mid, mid+1
        else:
            hi = mid-1
    return cand


def square_root(k):
    # return _linear_time_sq_root(k)
    return _log_time_sq_root(k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
