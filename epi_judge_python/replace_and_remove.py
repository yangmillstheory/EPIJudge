import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, a):
    '''Replace all "a" with two "d"'s and remove all "b"'s.

    Algorithm runs in O(n) time and O(1) space.'''
    # delete 'b' by moving everything to the front
    w_start = 0
    for i in range(size):
        if a[i] == 'b':
            continue
        a[w_start] = a[i]
        w_start += 1
    # white out any stale (now moved to front) entries
    for i in range(w_start, size):
        a[i] = ''
    w_end = n = w_start + a.count('a') - 1
    # replace 'a' by moving everything to the back
    for j in range(w_start-1, -1, -1):
        if a[j] == 'a':
            a[w_end] = a[w_end-1] = 'd'
            w_end -= 2
        else:
            a[w_end] = a[j]
            w_end -= 1
    return n+1


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
