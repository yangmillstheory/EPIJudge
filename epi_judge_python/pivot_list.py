import functools
from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def find(head, x):
    while head:
        if head.data == x:
            return head
        head = head.next


def list_pivoting(head, x):
    if not head:
        return
    mid = find(head, x)
    if not mid:
        return head
    lt = lt_dummy = ListNode(0)
    rt = rt_dummy = ListNode(0)
    while head:
        if head.data < x:
            lt.next = head
            lt = lt.next
        elif head.data > x:
            rt.next = head
            rt = rt.next
        head = head.next
    lt.next, rt.next = mid, None
    mid.next = rt_dummy.next
    return lt_dummy.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pivot_list.py", 'pivot_list.tsv',
                                       list_pivoting_wrapper))
