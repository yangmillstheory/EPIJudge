from test_framework import generic_test
from test_framework.test_failure import TestFailure


class QueueEmpty(RuntimeError):
    pass


class Queue:
    '''A dynamically resized Queue ADT.'''

    def __init__(self, capacity):
        assert isinstance(capacity, int) and capacity > 0
        self._head = 0
        self._tail = 0
        self._q = [None for _ in range(capacity)]

    def enqueue(self, x):
        '''Enqueue operation in amortized O(1) time.'''
        self._q[self._tail] = x
        self._tail += 1
        size = len(self._q)
        if self._tail == size:
            self._q += [None for _ in range(size)]

    def dequeue(self):
        '''Dequeue an element in O(1) time. Raises exception if queue was empty.'''
        if not self.size():
            raise QueueEmpty('Queue is empty!')
        x = self._q[self._head]
        self._head += 1
        return x

    def size(self):
        '''Returns the size of the queue.'''
        return self._tail-self._head


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
