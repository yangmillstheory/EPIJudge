from test_framework import generic_test


class Queue:
    def __init__(self):
        '''TODO: Docstring for __init__.

        :param f: TODO
        :returns: TODO
        '''
        self._push_stack = []
        self._pop_stack = []

    def enqueue(self, x):
        # T(n) = O(1)
        self._push_stack.append(x)

    def dequeue(self):
        # T(n) = O(n)
        self._ensure_pop_stack()
        return self._pop_stack.pop()

    def _ensure_pop_stack(self):
        if not self._pop_stack:
            while self._push_stack:
                self._pop_stack.append(self._push_stack.pop())


def queue_tester(ops):
    from test_framework.test_failure import TestFailure

    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_from_stacks.py",
                                       'queue_from_stacks.tsv', queue_tester))
