import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    WHITE, GRAY, BLACK = range(3)

    def __init__(self):
        self.edges = []
        self.color = self.WHITE


def is_deadlocked(graph):
    # T(n) = O(n)
    # S(n) = O(n)
    def dfs(v):
        v.color = GraphVertex.GRAY
        for u in v.edges:
            if u.color == GraphVertex.GRAY or (u.color == GraphVertex.WHITE and dfs(u)):
                return True
        v.color = GraphVertex.BLACK
        return False
    return any(dfs(v) for v in graph)


@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("deadlock_detection.py",
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))
