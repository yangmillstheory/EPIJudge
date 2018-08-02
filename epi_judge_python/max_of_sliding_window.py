import functools
from collections import deque
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class QueueWithMax(deque):
    def __init__(self):
        self._next_maxes = deque()

    def enqueue(self, x):
        self.append(x)
        while self._next_maxes and self._next_maxes[-1] < x:
            self._next_maxes.pop()
        self._next_maxes.append(x)

    def dequeue(self):
        x = self.popleft()
        if x == self.max():
            self._next_maxes.popleft()
        return x

    def max(self):
        if not self._next_maxes:
            raise ValueError('No max to return!')
        return self._next_maxes[0]


class TrafficElement:
    def __init__(self, time, volume):
        self.time = time
        self.volume = volume


def calculate_traffic_volumes(traffic, w):
    q, res = QueueWithMax(), []
    for t in traffic:
        while q and t.time - q[0][1] > w:
            q.dequeue()
        q.enqueue((t.volume, t.time))
        res.append(TrafficElement(t.time, q.max()[0]))
    return res


@enable_executor_hook
def calculate_traffic_volumes_wrapper(executor, A, w):
    A = [TrafficElement(t, v) for (t, v) in A]

    result = executor.run(functools.partial(calculate_traffic_volumes, A, w))

    return [(x.time, x.volume) for x in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_of_sliding_window.py",
                                       'max_of_sliding_window.tsv',
                                       calculate_traffic_volumes_wrapper))
