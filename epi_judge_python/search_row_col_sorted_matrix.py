from test_framework import generic_test


def matrix_search(g, x):
    if not g or not g[0]:
        return False
    m, n = len(g), len(g[0])
    i, j = 0, n-1
    while i < m and j >= 0:
        if g[i][j] == x:
            return True
        if g[i][j] < x:
            i += 1
        else:
            j -= 1
    return False



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
