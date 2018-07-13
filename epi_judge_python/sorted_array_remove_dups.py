import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(a):
    '''Remove duplicates from a sorted array in place in O(n) time.'''
    i = w = 0
    n = len(a)
    while i < n:
        while i and i < n and a[i] == a[i-1]:
            i += 1
        if i == n:
            break
        a[w] = a[i]
        i += 1
        w += 1
    return w


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
