from reverse_sublist import reverse_sublist
from test_framework import generic_test


def get_length(head):
    n = 0
    while head:
        head, n = head.next, n+1
    return n


def walk(head, n_steps):
    for _ in range(n_steps):
        head = head.next
    return head


def is_linked_list_a_palindrome(head):
    # T(n) = O(n)
    # S(n) = O(1)
    n = get_length(head)
    if n <= 1:
        return True
    s, n_steps = n//2 + 1, n//2
    if n % 2 != 0:
        s += 1
        n_steps += 1
    reverse_sublist(head, s, n)
    tail = walk(head, n_steps)
    is_pali = True
    node = head
    while node and tail:
        if node.data != tail.data:
            is_pali = False
            break
        node, tail = node.next, tail.next
    reverse_sublist(head, s, n)
    return is_pali


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
