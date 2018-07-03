from collections import deque
from test_framework import generic_test
from test_framework.test_failure import TestFailure


class QueueWithMax(deque):
    '''Queue with max API. Takes up O(n) extra space.'''

    def __init__(self):
        self._cands = deque()

    def enqueue(self, x):
        # T(n) = O(1) amortized?
        self.append(x)
        while self._cands and self._cands[-1] < x:
            # all previous and lesser candidates can never be the max.
            self._cands.pop()
        self._cands.append(x)

    def dequeue(self):
        # T(n) = O(1)
        x = self.popleft()
        if x == self._cands[0]:
            self._cands.popleft()
        return x

    def max(self):
        # T(n) = O(1)
        return self._cands[0] if self._cands else None


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_with_max.py",
                                       'queue_with_max.tsv', queue_tester))
