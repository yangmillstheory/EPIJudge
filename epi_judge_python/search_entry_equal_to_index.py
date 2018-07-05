import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def search_entry_equal_to_its_index(a):
    # T(n) = O(log n)
    # S(n) = O(1)
    lo, hi = 0, len(a)-1
    while lo <= hi:
        mid = lo + (hi-lo)//2
        if a[mid] == mid:
            return mid
        elif a[mid] < mid:
            lo = mid+1
        else:
            hi = mid-1
    return -1


@enable_executor_hook
def search_entry_equal_to_its_index_wrapper(executor, A):
    result = executor.run(
        functools.partial(search_entry_equal_to_its_index, A))
    if result != -1:
        if A[result] != result:
            raise TestFailure("Entry does not equal to its index")
    else:
        if any(i == a for i, a in enumerate(A)):
            raise TestFailure("There are entries which equal to its index")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_entry_equal_to_index.py",
            'search_entry_equal_to_index.tsv',
            search_entry_equal_to_its_index_wrapper))
