from list_node import ListNode
from test_framework import generic_test


def length(x):
    n = 0
    while x:
        n += 1
        x = x.next
    return n


def walk(head, n_steps):
    for _ in range(n_steps):
        head = head.next
    return head


def cyclically_right_shift_list(head, k):
    # T(n) = O(n)
    # S(n) = O(1)
    n = length(head)
    if not n or not k:
        return head
    k = k % n
    if not k:
        return head
    dummy = tail = ListNode(0, head)
    fast = walk(tail, k)
    while fast and fast.next:
        fast, tail = fast.next, tail.next
    fast.next, dummy.next, tail.next = dummy.next, tail.next, None
    return dummy.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
