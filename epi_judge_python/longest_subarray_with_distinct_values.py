from test_framework import generic_test


def longest_subarray_with_distinct_entries(xs):
    # T(n) = O(n)
    # S(n) = O(n)
    ind = {}
    s, max_length = 0, 0
    for j, x in enumerate(xs):
        if x in ind and ind[x] >= s:
            s = ind[x]+1
        ind[x] = j
        max_length = max(max_length, j-s+1)
    return max_length


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
