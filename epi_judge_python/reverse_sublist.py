from list_node import ListNode
from test_framework import generic_test


def get_kth(head, k):
    '''Returns the kth node from head (inclusive), 1-indexed.'''
    for _ in range(k-1):
        head = head.next
    return head


def reverse_sublist(head, s, f):
    '''Reverse a sublist of a singly-linked list in O(f) time.'''
    if not head:
        return
    if s == 1:
        prev_s, s_node = ListNode(0), head
    else:
        prev_s = get_kth(head, s-1)
        s_node = prev_s.next
    f_node = get_kth(s_node, f-s+1)
    while s_node != f_node:
        next_s_node, s_node.next = s_node.next, f_node.next
        f_node.next = s_node
        s_node = s_node.next
        s_node = next_s_node
    prev_s.next = f_node
    return prev_s.next if s == 1 else head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
