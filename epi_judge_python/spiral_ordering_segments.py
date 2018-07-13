import itertools
from test_framework import generic_test


def top(g, depth, n):
    for j in range(depth, n-depth-1):
        yield g[depth][j]


def right(g, depth, n):
    for i in range(depth, n-depth-1):
        yield g[i][-depth-1]


def bottom(g, depth, n):
    for j in reversed(range(depth+1, n-depth)):
        yield g[-depth-1][j]


def left(g, depth, n):
    for i in reversed(range(depth+1, n-depth)):
        yield g[i][depth]


def matrix_in_spiral_order(g):
    if not g or not g[0]:
        return []
    n = len(g)
    m = n//2
    it = itertools.chain(
        itertools.chain(top(g, depth, n), right(g, depth, n), bottom(g, depth, n), left(g, depth, n))
        for depth in range(m)
    )
    if n % 2:
        it = itertools.chain(it, [g[m][m]])
    return list(it)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
