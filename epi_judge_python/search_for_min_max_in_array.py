import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def min_max(x, y):
    return MinMax(x, y) if x < y else MinMax(y, x)


def find_min_max(a):
    '''Finds the min. and max. elements in a single pass with
    3n/2 comparisons and no extra space.'''
    n = len(a)
    if n == 1:
        return a[0], a[0]
    _min, _max = float('inf'), float('-inf')
    for i in range(0, n-1, 2):
        local_min_max = min_max(a[i], a[i+1])
        _min = min(_min, local_min_max.smallest)
        _max = max(_max, local_min_max.largest)
    if n % 2:
        _min = min(_min, a[-1])
        _max = max(_max, a[-1])
    return min_max(_min, _max)


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_min_max_in_array.py",
            'search_for_min_max_in_array.tsv',
            find_min_max,
            res_printer=res_printer))
