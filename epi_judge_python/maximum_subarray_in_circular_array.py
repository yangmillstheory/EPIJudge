from test_framework import generic_test


def find_optimal_sub(a, comparator):
    prev, max_seen = 0, 0
    for x in a:
        prev = comparator(prev+x, x)
        max_seen = comparator(prev, max_seen)
    return comparator(max_seen, 0)


def max_subarray_sum_in_circular(a):
    s = sum(a)
    return max(find_optimal_sub(a, max), s -find_optimal_sub(a, min))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "maximum_subarray_in_circular_array.py",
            'maximum_subarray_in_circular_array.tsv',
            max_subarray_sum_in_circular))
