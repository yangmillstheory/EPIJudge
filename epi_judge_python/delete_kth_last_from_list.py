from list_node import ListNode
from test_framework import generic_test


def walk(head, n_steps):
    for _ in range(n_steps):
        head = head.next
    return head


def remove_kth_last(head, k):
    dummy = slow = ListNode(0, head)
    fast = walk(dummy, k+1)
    while fast:
        slow, fast = slow.next, fast.next
    if slow.next:
        slow.next = slow.next.next
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
