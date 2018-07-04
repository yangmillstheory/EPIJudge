import functools
from collections import namedtuple
from posting_list_node import PostingListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def _jump_first_order_recursive(L, clones):
    if L in clones:
        return clones[L]
    clone = PostingListNode(L.order, None, None)
    clones[L] = clone
    clone.jump = _jump_first_order_recursive(L.jump, clones)
    clone.next = _jump_first_order_recursive(L.next, clones)
    return clone


def _jump_first_order_iterative(node):
    StackElement = namedtuple('StackElement', ['node', 'jump_from', 'next_from'])

    clones = {None: None}
    stack = [StackElement(node, None, None)]
    while stack:
        _node, jump_from, next_from = stack.pop()
        if not _node:
            continue
        if _node not in clones:
            clones[_node] = PostingListNode(_node.order, None, None)
        clone = clones[_node]
        if jump_from:
            jump_from.jump = clone
        if next_from:
            next_from.next = clone
        if _node.next not in clones or clone.next != clones[_node.next]:
            stack.append(StackElement(node=_node.next, jump_from=None, next_from=clone))
        if _node.jump not in clones or clone.jump != clones[_node.jump]:
            stack.append(StackElement(node=_node.jump, jump_from=clone, next_from=None))
    return clones[node]


def copy_postings_list(L):
    # return _jump_first_order_recursive(L, {None: None})
    return _jump_first_order_iterative(L)


def assert_lists_equal(orig, copy):
    node_mapping = dict()
    o_it = orig
    c_it = copy
    while o_it:
        if not c_it:
            raise TestFailure('Copied list has fewer nodes than the original')
        if o_it.order != c_it.order:
            raise TestFailure('Order value mismatch')
        node_mapping[o_it] = c_it
        o_it = o_it.next
        c_it = c_it.next

    if c_it:
        raise TestFailure('Copied list has more nodes than the original')

    o_it = orig
    c_it = copy
    while o_it:
        if c_it in node_mapping:
            raise TestFailure(
                'Copied list contains a node from the original list')
        if o_it.jump is None:
            if c_it.jump is not None:
                raise TestFailure(
                    'Jump link points to a different nodes in the copied list')
        else:
            if not node_mapping[o_it.jump] is c_it.jump:
                raise TestFailure(
                    'Jump link points to a different nodes in the copied list')
        o_it = o_it.next
        c_it = c_it.next


@enable_executor_hook
def copy_postings_list_wrapper(executor, l):
    def create_posting_list(serialized):
        key_mapping = dict()
        head = None
        for (order, _) in reversed(serialized):
            head = PostingListNode(order, head)
            key_mapping[order] = head

        list_it = head
        for (_, jump_index) in serialized:
            if jump_index != -1:
                list_it.jump = key_mapping.get(jump_index, None)
                if not list_it.jump:
                    raise RuntimeError('Jump index out of range')

        return head

    head = create_posting_list(l)

    copy = executor.run(functools.partial(copy_postings_list, head))

    assert_lists_equal(head, copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("copy_posting_list.py",
                                       'copy_posting_list.tsv',
                                       copy_postings_list_wrapper))
