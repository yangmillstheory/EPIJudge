import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(text, pat):
    '''Find the smallest subarray covering a set of words.

        T(t, p) = O(t)
        S(t, p) = O(p)
    '''
    n, j = len(text), 0
    counts, rem, sub = collections.Counter(), set(pat), None
    for i in range(n):
        if rem:
            # expand right to cover pat
            while j < n and rem:
                ch = text[j]
                if ch in pat:
                    counts[ch] += 1
                if ch in rem:
                    rem.remove(ch)
                j += 1
        if not rem and (not sub or j-1-i < sub.end-sub.start):
            sub = Subarray(i, j-1)
        ch = text[i]
        if ch in counts:
            counts[ch] -= 1
            if not counts[ch]:
                rem.add(ch)
                del counts[ch]
    return sub


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))
