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
    res = []
    for depth in range(m):
        res.extend(top(g, depth, n))
        res.extend(right(g, depth, n))
        res.extend(bottom(g, depth, n))
        res.extend(left(g, depth, n))
    if n % 2:
        res.append(g[m][m])
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
