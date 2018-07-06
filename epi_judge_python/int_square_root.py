from test_framework import generic_test


def _linear_time_sq_root(k):
    cand = 0
    for i in range(k+1):
        if pow(i, 2) <= k:
            cand = i
        else:
            break
    return cand


def square_root(k):
    return _linear_time_sq_root(k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
