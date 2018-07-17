from list_node import ListNode
from test_framework import generic_test


def add_two_numbers(x, y):
    dummy = node = ListNode(0)
    carry = 0
    while x or y or carry:
        x_data = x.data if x else 0
        y_data = y.data if y else 0
        s = x_data + y_data + carry
        if s >= 10:
            s -= 10
            carry = 1
        else:
            carry = 0
        node.next = ListNode(s)
        x = x or x.next
        y = y or y.next
        node = node.next
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
