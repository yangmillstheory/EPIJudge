import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def length(x):
    n = 0
    while x:
        n += 1
        x = x.next
    return n


def _overlapping_equal_length_lists(p, q):
    while p or q:
        if p is q:
            return p
        p = p and p.next
        q = q and q.next


def overlapping_no_cycle_lists(p, q):
    m, n = length(p), length(q)
    if m <= n:
        p, q, m, n = q, p, n, m
    for _ in range(m-n):
        p = p.next
    return _overlapping_equal_length_lists(p, q)


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
