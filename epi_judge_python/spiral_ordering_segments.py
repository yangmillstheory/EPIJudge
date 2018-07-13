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
    if n == 1:
        return [g[0][0]]
    it = itertools.chain.from_iterable([
        list(top(g, depth, n)) +
        list(right(g, depth, n)) +
        list(bottom(g, depth, n)) +
        list(left(g, depth, n))
        for depth in range(n//2)
    ])
    res = list(it)
    if n % 2:
        res.append(g[n//2][n//2])
    return res



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
