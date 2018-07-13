from test_framework import generic_test


def find_maximum_subarray(a):
    prev, max_seen = 0, float('-inf')
    for x in a:
        prev = max(prev+x, x)
        max_seen = max(prev, max_seen)
    return max(max_seen, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_sum_subarray.py",
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
