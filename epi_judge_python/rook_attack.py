import copy

from test_framework import generic_test


def rook_attack(g):
    m, n = len(g), len(g[0])
    row_1_0 = any(x == 0 for x in g[0])
    col_1_0 = any(g[i][0] == 0 for i in range(m))
    for i in range(1, m):
        for j in range(1, n):
            if g[i][j] == 0:
                g[0][j] = g[i][0] = 0

    def set_row_zero(i):
        for j in range(1, n):
            g[i][j] = 0

    def set_col_zero(j):
        for i in range(1, m):
            g[i][j] = 0

    for i in range(1, m):
        if g[i][0] == 0:
            set_row_zero(i)
    for j in range(1, n):
        if g[0][j] == 0:
            set_col_zero(j)
    if row_1_0:
        set_row_zero(0)
    if col_1_0:
        set_col_zero(0)
    if row_1_0 or col_1_0:
        g[0][0] = 0


def rook_attack_wrapper(A):
    a_copy = copy.deepcopy(A)
    rook_attack(a_copy)
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("rook_attack.py", 'rook_attack.tsv',
                                       rook_attack_wrapper))
