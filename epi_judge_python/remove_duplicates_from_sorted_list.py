from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(head):
    dummy = ListNode(0, head)
    p, q = dummy, dummy.next
    while p and q:
        while q.next and q.next.data == q.data:
            p.next = q.next
            q = q.next
        p, q = p.next, q.next
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
