import functools
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


DELIMITER = ' '


def reverse(seq, lo, hi):
    '''Reverse a sequence in O(hi-lo) time.'''
    while lo <= hi:
        seq[lo], seq[hi] = seq[hi], seq[lo]
        lo += 1
        hi -= 1


def reverse_words(b_array):
    '''Reverse words of a bytearray in O(W*w) time.'''
    n = len(b_array)
    reverse(b_array, 0, n-1)
    i = 0
    for j in range(n+1):
        if j == n or chr(b_array[j]) == DELIMITER:
            reverse(b_array, i, j-1)
            i = j+1


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
