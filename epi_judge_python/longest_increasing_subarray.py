import collections

from test_framework import generic_test

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_longest_increasing_subarray(a):
    s = Subarray(0, 0)
    i, n = 0, len(a)
    while i < n:
        j = i
        while j < n:
            if j+1 == n or a[j] >= a[j+1]:
                break
            j += 1
        if j-i >= s[1]-s[0]:
            s = Subarray(i, j)
        i = j+1
    return s


def find_longest_increasing_subarray_wrapper(A):
    result = find_longest_increasing_subarray(A)
    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_increasing_subarray.py",
            'longest_increasing_subarray.tsv',
            find_longest_increasing_subarray_wrapper))
