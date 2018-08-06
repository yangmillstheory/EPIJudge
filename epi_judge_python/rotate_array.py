import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def rotate_array(k, a):
    '''Rotate an array in O(n) time and O(1) space.'''
    n = len(a)
    k %= n
    i = t = 0
    while i < k and t < n:
        prev = a[i]
        j = (i+k) % n
        while t < n:
            temp = a[j]
            a[j], prev = prev, temp
            t += 1
            if j == i:
                # need this here instead of the loop
                # condition since we want to swap into i
                break
            j = (j+k) % n
        i += 1


@enable_executor_hook
def rotate_array_wrapper(executor, A, rotate_amount):
    a_copy = A[:]
    executor.run(functools.partial(rotate_array, rotate_amount, a_copy))
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("rotate_array.py", 'rotate_array.tsv',
                                       rotate_array_wrapper))
