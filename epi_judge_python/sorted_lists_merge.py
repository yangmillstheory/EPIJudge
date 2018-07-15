from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(p, q):
    head = prev = ListNode(0)
    while p and q:
        if p.data < q.data:
            prev.next, p = p, p.next
        else:
            prev.next, q = q, q.next
        prev = prev.next
    if p:
        prev.next = p
    elif q:
        prev.next = q
    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
