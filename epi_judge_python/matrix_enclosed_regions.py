from test_framework import generic_test


_mark, white, black = object(), 'W', 'B'


def fill_surrounded_regions(g):
    # T(m,n) = S(m,n) = O(m*n)
    if not g or not g[0]:
        raise ValueError
    m, n = len(g), len(g[0])

    def mark_ws(i, j):
        g[i][j] = _mark
        for x, y in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
            if min(x, y) < 0 or x >= m or y >= n or g[x][y] != white:
                continue
            mark_ws(x, y)
    for i in range(m):
        if g[i][0] == white:
            mark_ws(i, 0)
        if g[i][n-1] == white:
            mark_ws(i, n-1)
    for j in range(n):
        if g[0][j] == white:
            mark_ws(0, j)
        if g[m-1][j] == white:
            mark_ws(m-1, j)
    for i in range(m):
        for j in range(n):
            if g[i][j] == white:
                g[i][j] = black
            elif g[i][j] == _mark:
                g[i][j] = white


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
